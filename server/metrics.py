import os, sys

from core.base import VAULTObject

class Metrics(VAULTObject):
    def __init__(self, json:dict) -> None:
        super().__init__(json)

        