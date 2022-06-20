import os, sys
from errors import InvalidJSONDocument

from core.file import File

class Book(File):
    def __init__(self, json) -> None:
        super().__init__(json)

        self.validate()

        self.book_info = self.get_json()["book_info"]

        self.book_title = self.get_json()["book_title"]
        self.book_author = self.get_json()["book_author"]
        self.book_format = self.get_json()["book_format"]
        self.page_count = self.get_json()["page_count"]

    def validate(self):
        if "book_info" not in self.get_json().keys():
            raise InvalidJSONDocument("JSON Document is not a book")