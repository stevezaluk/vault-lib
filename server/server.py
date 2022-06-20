import os, sys, requests

from ..connection.database import Database
from ..connection.plex import Plex
from ..connection.http import HTTPConnection

from ..media_types import generate_object

class VAULTServer(HTTPConnection):
    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port

        self.base_url = "http://{i}:{p}/api/v1/".format(i=self.ip_address, p=self.port)
        super(VAULTServer, self).__init__(self.base_url)

    def search(self, q, section=None, limit=20):
        if section:
            endpoint = "search/{}".format(section)
        else:
            endpoint = "search"

        resp = self.query(endpoint, params={"q":q, "limit":limit})

    def index(self, section=None, limit=20):
        if section:
            endpoint = "index/{s}".format(s=section)
        else:
            endpoint = "index"

        resp = self.query(endpoint, params={"limit":limit})

        # convert to object

    def get_file(self, term, section=None):
        if section:
            endpoint = "file/{s}/{t}".format(s=section, t=term)
        else:
            endpoint = "file/{}".format(term)

        resp = self._query(endpoint)

        return generate_object(resp)

    def get_sections(self, limit=5):
        sections = []
        endpoint = "sections"

        resp = self._query(endpoint)

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

class LocalVAULTServer(object):
    def __init__(self, ip_address: str, port: int, database: Database, plex: Plex) -> None:
        self.ip_address = ip_address
        self.port = port

        self.database = database
        self.plex = plex

    def connect(self):
        self.database.connect()
        self.plex.connect()

    def disconnect(self):
        self.database.disconnect()
        self.plex.disconnect()

    def search(self, term, section=None):
        pass

    def index(self):
        pass

    def get_file(self, term):
        pass

    def get_sections(self):
        pass

    def get_section(self, section):
        pass

    def upload(self):
        pass

    def download(self):
        pass

    def remove(self):
        pass

    def archive(self):
        pass

    def status_change(self):
        pass