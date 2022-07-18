from json import loads
from bson.json_util import dumps

from ..connection.database import Database
from ..connection.plex import Plex

from ..media_types import generate_object

class VAULTServer(object): # change to vaultserver
    def __init__(self, mongo_ip: str, mongo_port: int, plex_ip: str, plex_port: int, plex_token: str) -> None:
        self.mongo_ip = mongo_ip
        self.mongo_port = mongo_port

        self.plex_ip = plex_ip
        self.plex_port = plex_port
        self.plex_token = plex_token

        self.database = Database(self.mongo_ip, self.mongo_port)
        self.plex = Plex(self.plex_ip, self.plex_port, self.plex_token)

    def connect(self):
        self.database.connect()
        self.plex.connect()

    def disconnect(self):
        self.database.disconnect()
        self.plex.disconnect()

    def _dict_to_response(self, dict: dict):
        if dict is None:
            json = {}

        return loads(dumps(dict, default=str))

    def search(self, file_name: str, section_name=None, key=None, limit=15, to_dict=False): # add to_dict paramater for just returning the dictionary after _dict_to_reponse is called
        ret = []

        if section_name is None:
            sections = self.get_sections()

            for section in sections:
                collection = self.database.get_collection(self.database.vault_db, section.section_name)
                documents = self.database.find(collection, {})

                for document in documents:
                    document = self._dict_to_response(document)
                    if file_name in document["file_name"]:
                        if (key is not None and key in document.keys()):
                            ret.append(document[key])
                        else:
                            if to_dict:
                                ret.append(document)
                            else:
                                ret.append(generate_object(document))
        else:
            section = self.get_section(section_name)
            if section is None:
                return None

            collection = self.database.get_collection(self.database.vault_db, section.section_name)
            documents = self.database.find(collection, {})

            for document in documents:
                document = self._dict_to_response(document)
                if file_name in document["file_name"]:
                    if (key is not None and key in document.keys()):
                        ret.append(document[key])
                    else:
                        if to_dict:
                            ret.append(document)
                        else:
                            ret.append(generate_object(document))

        return ret

    def index(self, section_name=None, key=None, limit=15, to_dict=False):
        ret = []

        if section_name is None:
            sections = self.get_sections()

            for section in sections:
                collection = self.database.get_collection(self.database.vault_db, section.section_name)
                documents = self.database.find(collection, {})

                for document in documents:
                    document = self._dict_to_response(document)

                    if (key is not None and key in document.keys()):
                        ret.append(document[key])
                    else:
                        if to_dict:
                            ret.append(document)
                        else:
                            ret.append(generate_object(document))
        else:
            section = self.get_section(section_name)
            if section is None:
                return None # change this to false

            collection = self.database.get_collection(self.database.vault_db, section.section_name)
            documents = self.database.find(collection, {})

            for document in documents:
                document = self._dict_to_response(document)

                if (key is not None and key in document.keys()):
                    ret.append(document[key])
                else:
                    if to_dict:
                        ret.append(document)
                    else:
                        ret.append(generate_object(document))
        # write limit
                
        return ret

    def get_file(self, term: str, section_name=None, key=None, no_plex=False, to_dict=False):
        document = None
        query = self.database.build_db_query(term)

        if section_name is None:
            sections = self.get_sections()
            for section in sections:
                collection = self.database.get_collection(self.database.vault_db, section.section_name) # change to use mongo_collection key instead
                document = self.database.find_one(collection, query)
                
                if document is not None:
                    break
        else:
            section = self.get_section(section_name)
            if section is None:
                return None

            collection = self.database.get_collection(self.database.vault_db, section.section_name)
            document = self.database.find_one(collection, query)

        if document is None:
            return None
        
        document = self._dict_to_response(document)
        keys = document.keys()

        if no_plex is False:
            if "file_name" in keys: # methodize this
                name = document["file_name"]
            elif "directory_name" in keys:
                name = document["directory_name"]

            plex_item, plex_key = self.plex.get_item_key(name)
            if plex_key:
                plex_metadata = {"title":plex_item.title, "type": plex_item.type, "description":plex_item.summary, "content_rating":plex_item.contentRating, "user_rating":plex_item.userRating, "plex_section":plex_item.librarySectionTitle, "added_at":str(plex_item.addedAt), "updated_at":str(plex_item.updatedAt), "view_count":plex_item.viewCount}
                document.update({"plex_info":plex_metadata})

        if to_dict:
            ret = document
        else:
            ret = generate_object(document)
        
        return ret

    def get_sections(self, key=None, limit=15, to_dict=False):
        ret = []
        
        sections = self.database.get_collection(self.database.vault_db, "sections")
        for document in self.database.find(sections, {}):
            document = self._dict_to_response(document)
            
            if (key is not None and key in document.keys()):
                ret.append(document[key])
            else:
                if to_dict:
                    ret.append(document)
                else:
                    ret.append(generate_object(document))
            
        return ret

    def get_section(self, section_name: str, key=None, to_dict=False):
        sections = self.database.get_collection(self.database.vault_db, "sections")
        
        section = self.database.find_one(sections, {"section_name": section_name})
        if section is None:
            return None
        
        document = self._dict_to_response(section)

        if (key is not None and key in document.keys()):
            ret = document[key]
        else:
            if to_dict:
                ret = document
            else:
                ret = generate_object(document)
        
        return ret

    def upload(self, path: str, section_name=None):
        pass

    def download(self, term: str, section_name=None):
        file = self.get_file(term, section_name=section_name)
        if file is None:
            raise FileNotFoundError("Failed to find file for download: {}".format(term))

    def remove(self, hash: str, section_name=None):
        pass

    def archive(self, hash: str, section_name=None):
        pass

    def status_change(self):
        pass