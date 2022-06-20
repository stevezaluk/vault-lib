import os, sys

from ..errors import InvalidJSONStructure

class VAULTObject(object):
	def __init__(self, json):
		self.__json = json
		self.__id = None

		self.keys = ["file_name", "file_size", "file_location",
						"file_type", "file_section", "file_sha",
						"file_status", "uploaded_by", "uploaded_date", 
						"media_info", "video_codec", "audio_codec", 
						"video_codec_lib", 
						"duration", "resolution", "creation_date"]

		self.structure_check()
	
	def get_json(self):
		return self.__json

	def get_object_id(self):
		return self.__id

	def structure_check(self):
		for key in self.get_json():
			if key not in self.keys:
				raise InvalidJSONStructure("JSON Document is missing keys or has too many")
