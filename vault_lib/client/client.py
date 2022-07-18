from ..connection.http import HTTPConnection
from ..media_types import generate_object


"""
    Client side representation of a VAULT server
    
    Makes HTTP requests to the VAULT Rest API
"""
class VAULTClient(HTTPConnection): # change to vaultclient
    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port

        self.base_url = "http://{i}:{p}/api/v1/".format(i=self.ip_address, p=self.port)
        super(VAULTClient, self).__init__(self.base_url)

    def search(self, q, section=None, limit=15):
        ret = []
        if section:
            endpoint = "search/{}".format(section)
        else:
            endpoint = "search"

        resp = self._query(endpoint, params={"q":q, "limit":limit})
        resp = resp["search"]

        for result in resp:
            ret.append(generate_object(result))

        return ret

    def index(self, section=None, limit=15):
        ret = []
        if section:
            endpoint = "index/{s}".format(s=section)
        else:
            endpoint = "index"

        resp = self._query(endpoint, params={"limit":limit})
        resp = resp["index"]

        for result in resp:
            ret.append(generate_object(result))

        return ret

        # convert to object

    def get_file(self, term, section=None):
        if section: # methodize this block
            endpoint = "file/{s}/{t}".format(s=section, t=term)
        else:
            endpoint = "file/{}".format(term)

        resp = self._query(endpoint)

        return generate_object(resp)

    def get_sections(self, limit=15):
        sections = []
        endpoint = "sections"

        resp = self._query(endpoint)
        resp = resp["sections"]

        for section in resp:
            sections.append(generate_object(section))

        return sections
        # convert ot object

    def get_section(self, section):
        endpoint = "sections/{}".format(section)

        resp = self._query(endpoint)

        return generate_object(resp)

    def upload(self, path: str, background_checks=True):
        pass

    def download(self):
        pass

    def remove(self):
        pass

    def archive(self):
        pass

    def status_change(self):
        pass

    def metrics(self, section=None):
        if section:
            endpoint = "metrics"
        else:
            endpoint = "metrics/{}".format(section)
    
    def standards(self):
        endpoint = "standards"
