class InvalidJSONStructure(Exception):
	def __init__(self, message):
		super().__init__(message)

class InvalidJSONDocument(Exception):
	def __init__(self, message):
		super().__init__(message)

class MissingDatabase(Exception):
	def __init__(self, message):
		super().__init__(message)

class MissingCollection(Exception):
	def __init__(self, message):
		super().__init__(message)

class VAULTFileNotFound(Exception):
	def __init__(self, message):
		super().__init__(message)

class VAULTInternalServerError(Exception):
	def __init__(self, message):
		super().__init__(message)

class VAULTUnauthorized(Exception):
	def __init__(self, message):
		super().__init__(message)

class VAULTWrongContentType(Exception):
	def __init__(self, message):
		super().__init__(message)

class LocalFileNotFound(Exception):
	def __init__(self, message):
		super().__init__(message)