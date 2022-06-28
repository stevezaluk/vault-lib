import os, sys

from ..core.base import VAULTObject
from ..errors import InvalidJSONDocument, LocalFileNotFound

class File(VAULTObject):
	def __init__(self, json:dict):
		super(File, self).__init__(json)

		self.validate()

		print("file")
		self.file_name = self.get_json()["file_name"]
		self.file_size = self.get_json()["file_size"]
		self.file_type = self.get_json()["file_type"]
		self.file_section = self.get_json()["file_section"]

		self.file_sha = self.get_json()["file_sha"]
		self.file_status = self.get_json()["file_status"]

		self.uploaded_by = self.get_json()["uploaded_by"]
		self.uploaded_date= self.get_json()["uploaded_date"]
		self.creation_date = self.get_json()["creation_date"]

	def validate(self):
		if "file_name" not in self.get_json().keys():
			raise InvalidJSONDocument("JSON Document is not a file document")

class MediaFile(File):
	def __init__(self, json):
		super(MediaFile, self).__init__(json)

		self.validate()
		print("media_file")

		self._media_info = self.get_json()["media_info"]

		self.resolution = self._media_info["resolution"]
		self.duration = self._media_info["duration"]
		self.video_codec = self._media_info["video_codec"]
		self.video_codec_lib = self._media_info["video_codec_lib"]
		self.audio_codec = self._media_info["audio_codec"]
		self.languages = self._media_info["languages"]

	def validate(self):
		if "media_info" not in self.get_json().keys():
			raise InvalidJSONDocument("JSON Document is not a media file")

class PlexFile(MediaFile):
	def __init__(self, json):
		super().__init__(json)

		self.validate()

		self.plex_info = self.get_json()["plex_info"]

		self.title = self.plex_info["title"]
		self.description = self.plex_info["description"]
		self.content_rating = self.plex_info["content_rating"]
		self.user_rating = self.plex_info["user_rating"]

		self.plex_episode_count = None
		self.plex_season_count = None

	def validate(self):
		if "plex_info" not in self.get_json().keys():
			raise InvalidJSONDocument("Error Document is not a plex file")

class LocalFile(object):
	def __init__(self, path):
		self.path = path

		self.validate()

	def validate(self):
		if self.path.startswith("~"):
			self.path = self.path.replace("~", os.getenv("HOME"))
		
		if os.path.exists(self.path) is False:
			raise LocalFileNotFound("Local file could not be found: " + self.path)