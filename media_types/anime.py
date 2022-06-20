import os, sys

from ..media_types.tv_show import TVShow
from ..errors import InvalidJSONDocument

class Anime(TVShow):
    def __init__(self, json: dict):
        super(Anime, self).__init__(json)

        self.validate()
        
        self.dub_status = self.tv_info["dub_status"]

    def validate(self):
        if "dub_status" not in self.tv_info.keys():
            raise InvalidJSONDocument("JSON Document is not a anime")