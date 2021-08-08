from telegrask import Telegrask
from .config import CLIENT_ID, CLIENT_SECRET, TOKEN
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

spotify = Spotify(auth_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))
bot = Telegrask(TOKEN)

from . import commands
