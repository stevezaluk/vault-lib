import os, sys

from ..core.directory import Directory
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