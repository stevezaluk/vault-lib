import os, sys

from ..core.base import VAULTObject
from ..errors import InvalidJSONDocument

class Directory(VAULTObject):
    def __init__(self, json: dict):
        super(VAULTObject, self).__init__(json)

        self.validate()

        self.directory_name = self.get_json()["directory_name"]
        self.directory_parent = Directory(self.get_json()["directory_parent"])
        self.directory_size = self.get_json()["directory_size"]

        self.directory_section = self.get_json()["directory_section"]
        self.directory_status = self.get_json()["directory_status"]

        self.uploaded_date = self.get_json()["uploaded_date"]
        self.uploaded_by = self.get_json()["uploaded_by"]
        self.creation_date = self.get_json()["creation_date"]

        # self.contents

    def validate(self):
        if "directory_name" not in self.get_json().keys():
            raise InvalidJSONDocument("JSON Document is not a directory")