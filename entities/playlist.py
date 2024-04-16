import json
import logging

from config.config import URL_SPOTIFY, USER_SPOTIFY
from helpers.rest_client import RestClient
from utils.logger import get_logger
from datetime import datetime

LOGGER = get_logger(__name__, logging.DEBUG)

# ts stores the time in order to have a Playlist name distinguisable
current_datetime = datetime.now()
ts = current_datetime.strftime("%H:%M:%S, %b %d %Y")

class Playlist:

    def __init__(self, rest_client=None):
        self.url_playlists = f"{URL_SPOTIFY}/playlists"
        if rest_client is None:
            self.rest_client = RestClient()

    def create_playlist(self, body=None):
        body_project = body
        if body is None:
            body_playlist = {
                "name": f"New Playlist #{ts} (No Fixture)",
                "description": f"New playlist description #{ts} (No Fixture)"
            }
        url_create_playlist = f"{URL_SPOTIFY}/users/{USER_SPOTIFY}/playlists"
        response = self.rest_client.request("post", url=url_create_playlist, body=json.dumps(body_playlist))

        return response, self.rest_client