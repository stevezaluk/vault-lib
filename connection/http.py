import os, sys, requests, json
from ossaudiodev import control_names

from errors import *

class HTTPConnection(object):
  def __init__(self, base_url):
    self.base_url = base_url

  def _query(self, endpoint, params=None, content_type="application/json"):
    url = self.base_url + endpoint
    resp = requests.get(url, params=params)

    if resp.status_code == 404:
      raise VAULTFileNotFound("Failed to find resource")

    if resp.status_code == 401:
      raise VAULTUnauthorized("Unauthorized user.")

    if resp.status_code == 500:
      raise VAULTInternalServerError("Internal Server error") 

    ct = resp.headers["Content-Type"]

    if ct != content_type:
      raise VAULTWrongContentType("Wrong content type: ", ct)

    if ct == "application/json":
      return json.loads(resp.content)
    elif ct.startswith("video"):
      return resp.content



