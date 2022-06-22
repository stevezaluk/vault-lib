import os, sys

from ..core.file import MediaFile, PlexFile, File
from ..media_types.game import GameFile

def generate_object(json: dict):
    keys = json.keys()
    if "plex_info" in keys:
        return PlexFile(json)
    elif "media_info" in keys:
        return MediaFile(json)
    elif "game_info" in keys:
        return GameFile(json)
    elif "course_info" in keys:
        return 