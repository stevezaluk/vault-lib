import os, sys

from ..core.file import File
from ..errors import InvalidJSONDocument

class Game(File):
    def __init__(self, json):
        super().__init__(json)

        self.validate()

        self.game_info = self.get_json()["game_info"]

        self.console = self.game_info["console"]
        self.region = self.game_info["region"]

    def validate(self):
        if "game_info" not in self.get_json().keys():
            raise InvalidJSONDocument("JSON Document is not a game")