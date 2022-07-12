import os, sys

class VAULTObject(object):
	def __init__(self, json):
		self.__json = json
		self.__id = None

	def get_json(self):
		return self.__json

	def get_object_id(self):
		return self.__id
