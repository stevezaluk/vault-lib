import os, sys

from ..core.file import MediaFile, PlexFile, File
from ..media_types.game import GameFile
from ..media_types.book import Book

from ..media_types.tv_show import TVShow, TVEpisode

from ..server.section import Section

def generate_object(json: dict):
    keys = json.keys()

    ret = None
    for key in keys:
        if key == "section_name":
            return Section(json)
        
        if key == "plex_info":
            ret = PlexFile(json)

        if key == "media_info":
            ret = MediaFile(json)

        if key == "tv_info":
            ret = TVShow(json)

        if key == "episode_info":
            ret = TVEpisode(json)

        if key == "game_info":
            ret = GameFile(json)

        if key == "book_info":
            ret = Book(json)

    return ret