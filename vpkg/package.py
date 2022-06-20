import os, json

from core.base import VAULTObject

class Package(VAULTObject):
    def __init__(self, json: dict):
        super(Package, self).__init__(json)

        self.validate()

        self.package_name = self.get_json()["package_name"]
        self.package_homepage = self.get_json()["package_homepage"]
        self.package_author = self.get_json()["package_author"]
        self.package_description = self.get_json()["package_description"]
        self.package_module = self.get_json()["package_module"]

        self.operating_systems = self.get_json()["operating_systems"]
        self.associated_files = self.get_json()["associated_files"]

    def validate(self):
        pass