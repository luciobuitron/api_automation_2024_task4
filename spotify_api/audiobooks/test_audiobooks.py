import json
import logging
import pytest

from config.config import URL_SPOTIFY
from utils.logger import get_logger
from helpers.rest_client import RestClient
from datetime import datetime

LOGGER = get_logger(__name__, logging.DEBUG)

# ts stores the time in order to have a Playlist name distinguisable
current_datetime = datetime.now()
ts = current_datetime.strftime("%H:%M:%S, %b %d %Y")

class TestPlaylists:
    @classmethod
    def setup_class(cls):
        LOGGER.debug("Setup Class method")
        cls.url_audiobooks = f"{URL_SPOTIFY}/me/audiobooks"
        cls.list_audiobooks = []
        cls.rest_client = RestClient()

    @pytest.mark.acceptance
    def test_get_user_audiobooks(self, log_test_name):
        """
        Test get user audiobooks
        Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.
        """

        # Generating a new code value for authentication/authorization
        # from config.authentication import spotify_authentication
        # with authentication.test_request_context('/login'):
        #     authentication.preprocess_request()
        #     spotify_authentication()

        response = self.rest_client.request("get", url=self.url_audiobooks)

        assert response["status_code"] == 200, "Wrong status code, expected 200"