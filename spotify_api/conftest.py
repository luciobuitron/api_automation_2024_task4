import json
import logging

import time
import pytest
import requests

from datetime import datetime
from config.config import URL_SPOTIFY, USER_SPOTIFY
from utils.logger import get_logger
from helpers.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)

# ts stores the time in order to have a Playlist name distinguisable
current_datetime = datetime.now()
ts = current_datetime.strftime("%H:%M:%S, %b %d %Y")

@pytest.fixture(name="create_playlist")
def create_playlist(request):
    """
    Fixture to create a new playlist
    :param request:
    :return:
    """

    LOGGER.debug("Create playlist From Fixture")
    body_playlist = {
        "name": f"New Playlist #{ts} (From Fixture)",
        "description": f"New Playlist description #{ts} (From Fixture)",
        "public": True
    }
    url_playlist = URL_SPOTIFY+"/users/"+USER_SPOTIFY+"/playlists"
    rest_client = RestClient()
    response = rest_client.request("post", url_playlist, body=json.dumps(body_playlist))

    return response
    # Not possible to delete the created playlist using yield
    # or implementing a method since it is now allowed by Spotify

@pytest.fixture(name="get_playlist")
def get_playlist():
    """
    Fixture to get playlist
    :return:
    """
    rest_client = RestClient()
    response = rest_client.request("get", URL_SPOTIFY+"/users/"+USER_SPOTIFY+"/playlists")
    playlist_name = response["body"]["items"][1]["name"]
    LOGGER.info("Playlist name: %s", playlist_name)

    return playlist_name


@pytest.fixture()
def log_test_name(request):
    """
    Fixture to Log the test names in logs
    :param request:     Object to get the test node name
    """
    LOGGER.info("---------- TEST '%s' STARTED.---------- ", request.node.name)
    def fin():
        LOGGER.info("----------  TEST'%s' COMPLETED.---------- ", request.node.name)

    request.addfinalizer(fin)
