import os, sys, re

from bson import ObjectId

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from errors import MissingCollection, MissingDatabase

class Database(object):
    def __init__(self, ip_address: str, port: int):
        self.ip_address = ip_address
        self.port = port

        self._client = None

        self.vault_db = self.get_database("vaultdb")
        self.archive_db = self.get_database("archivedb")
        self.metrics_db = self.get_database("metricsdb")

    def connect(self):
        if self._client is None:
            self._client = MongoClient(self.ip_address, self.port)
        
    def disconnect(self):
        if self._client is not None:
            self._client.close()

    def get_client(self):
        return self._client

    def get_database_names(self):
        return self._client.list_database_names()

    def get_collection_names(self, database: Database):
        return database.list_collection_names()
    
    def get_database(self, database: str):        
        for database_name in self.get_database_names():
            if database_name == database:
                return self._client[database_name]

        raise MissingDatabase("Database {} could not be found. Use vault-build to rebuild it".format(database))

    def get_collection(self, database: Database, collection: str):
        for collection_name in self.get_collection_names(database):
            if collection_name == collection:
                return database[collection_name]
            
        raise MissingCollection("Collection {} could not be found. Use vault-build to rebuild it")
    
    def find_one(self, collection: Collection, query: dict):
        return collection.find_one(query)

    def find_one_by_id(self, collection: Collection, id: str):
        return collection.find_one({"_id":ObjectId(id)})

    def insert_one(self, collection: Collection, doc: dict):
        return collection.insert_one(doc)
    
    def search_collection(self, collection: Collection, query: dict):
        pass

    def build_db_query(self, term):
        db_query = {}

        regex = re.compile(r'\b[A-Fa-f0-9]{64}\b')
        if regex.match(term):
            db_query.update({"file_sha":term})
        elif ObjectId.is_valid(term):
            db_query.update({"_id":ObjectId(term)})
        else:
            db_query.update({"file_name":term})

        return db_query
        