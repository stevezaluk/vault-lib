import os, sys

from ..core.directory import Directory
from ..core.file import MediaFile
from ..errors import InvalidJSONDocument

class TVShow(Directory):
	def __init__(self, json: dict):
		super(TVShow, self).__init__(json)

		self.validate()

		self.tv_info = self.get_json()["tv_info"]
		
		self.season_count = self.tv_info["season_count"]
		self.episode_count = self.tv_info["episode_count"]
		self.average_duration = self.tv_info["average_duration"]

	def validate(self):
		if "tv_info" not in self.get_json().keys():
			raise InvalidJSONDocument("JSON Document is not a TV show")

class TVEpisode(MediaFile):
	def __init__(self, json):
		super(TVEpisode, self).__init__(json)

		self.validate()

		self.episode_info = self.get_json()["epsiode_info"]

		self.season_number = self.episode_info["season_number"]
		self.episode_number = self.episode_info["episode_number"]

		# self.parent

	def validate(self):
		if "episode_info" not in self.get_json().keys():
			raise InvalidJSONDocument("JSON Document is not a episode")

class Anime(TVShow):
    def __init__(self, json: dict):
        super(Anime, self).__init__(json)

        self.validate()
        
        self.dub_status = self.tv_info["dub_status"]

    def validate(self):
        if "dub_status" not in self.tv_info.keys():
            raise InvalidJSONDocument("JSON Document is not a anime")

