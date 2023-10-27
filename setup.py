#Description: setup.py holds the credentials for the Spotify API. It also initializes the spotipy object, sp
#that we will use to interact with the API.


import spotipy as spot
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

#credentials from Spotify for Developers
client_id = 'dc4aa95b1a7d4aa3add2c3f53c827c03'
client_secret = '250c1166095347c5a64daf2e1b838afa'
redirect_uri = 'https://example.com/callback'

sp = spot.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-modify-public'))

#save my personal URI
MichaelNocerino_uri = 'spotify:user:12143795131'