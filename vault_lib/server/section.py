import os, sys

from ..core.base import VAULTObject
from ..errors import InvalidJSONDocument

class Section(VAULTObject):
    def __init__(self, json):
        super().__init__(json)

        self.validate()

        self.section_name = self.get_json()["section_name"]
        self.section_path = self.get_json()["section_path"]
        self.section_type = self.get_json()["section_type"]
        
        
        self.total_files = self.get_json()["total_files"]
        self.total_downloads = self.get_json()["total_downloads"]
        self.total_uploads = self.get_json()["total_uploads"]
        self.total_archives = self.get_json()["total_archives"]

    def validate(self):
        if "section_name" not in self.get_json().keys():
            raise InvalidJSONDocument("JSON Document is not a section")