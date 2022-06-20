import os, sys
from ..errors import InvalidJSONDocument

from ..core.file import MediaFile
from ..media_types.tv_show import TVShow

class Episode(MediaFile):
	def __init__(self, json):
		super(Episode, self).__init__(json)

		self.validate()

		self.episode_info = self.get_json()["epsiode_info"]

		self.season_number = self.episode_info["season_number"]
		self.episode_number = self.episode_info["episode_number"]

		# self.parent

	def validate(self):
		if "episode_info" not in self.get_json().keys():
			raise InvalidJSONDocument("JSON Document is not a episode")