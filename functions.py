#functions.py contains a series of functions that give a user insight 
#to shared music with friends.

#import objects from our setup file
from setup import client_id
from setup import client_secret
from setup import redirect_uri
from setup import sp




#Shared Songs:
#takes in two usernames and provides a list of all songs in common
#between the two user's public playlists

def sharedSongs(userOne, userTwo):
  
  userOneResults = sp.user_playlists(userOne)
  userOnePlaylists = []
  for dictionary in userOneResults['items']:
    if 'id' in dictionary.keys():
      userOnePlaylists.append(dictionary['id'])

  userOneSongs = []
  for playlist in userOnePlaylists:
    s_playlist = sp.user_playlist_tracks(userOne, playlist)

    #s_playlist['items'] is a list of dictionarys
    for track in s_playlist['items']:
      if track['track']['name'] not in userOneSongs:
        userOneSongs.append(track['track']['name'])

  userTwoResults = sp.user_playlists(userTwo)
  userTwoPlaylists = []
  for dictionary in userTwoResults['items']:
    if 'id' in dictionary.keys():
      userTwoPlaylists.append(dictionary['id'])

  userTwoSongs = []
  for playlist in userTwoPlaylists:
    s_playlist = sp.user_playlist_tracks(userTwo, playlist)

    #s_playlist['items'] is a list of dictionarys
    for track in s_playlist['items']:
      if track['track']['name'] not in userTwoSongs:
        userTwoSongs.append(track['track']['name'])

  #now scan the two artist lists with a double for loop to find intersection
  #of the two sets
  shared = []
  for song in userOneSongs:
    if song in userTwoSongs:
      shared.append(song)
  #output the shared artists
  print(len(shared), "Shared Songs:")
  for item in shared:
    print(item)

#test the function
sharedSongs(12143795131, 'mocolvin')



#Shared Artists:
##this function returns the common Artists known by the two individuals
#userOne, userTwo are integers that represent the userID of the individual

def sharedArtists(userOne, userTwo):

  userOneResults = sp.user_playlists(userOne)
  userOnePlaylists = []
  for dictionary in userOneResults['items']:
    if 'id' in dictionary.keys():
      userOnePlaylists.append(dictionary['id'])

  userOneArtists = []
  for playlist in userOnePlaylists:
    s_playlist = sp.user_playlist_tracks(userOne, playlist)

    #s_playlist['items'] is a list of dictionarys
    for track in s_playlist['items']:
      if track['track']['album']['artists'][0]['name'] not in userOneArtists:
        userOneArtists.append(track['track']['album']['artists'][0]['name'])

  userTwoResults = sp.user_playlists(userTwo)
  userTwoPlaylists = []
  for dictionary in userTwoResults['items']:
    if 'id' in dictionary.keys():
      userTwoPlaylists.append(dictionary['id'])

  userTwoArtists = []
  for playlist in userTwoPlaylists:
    s_playlist = sp.user_playlist_tracks(userTwo, playlist)

    #s_playlist['items'] is a list of dictionarys
    for track in s_playlist['items']:
      if track['track']['album']['artists'][0]['name'] not in userTwoArtists:
        userTwo.append(track['track']['album']['artists'][0]['name'])


  #now scan the two artist lists with a double for loop to find intersection
  #of the two sets
  shared = []
  for artist in userOneArtists:
    if artist in userTwoArtists:
      shared.append(artist)
  #output the shared artists
  print(len(shared), "Shared Artists:")
  for item in shared:
    print(item)

#test the SharedArtists
sharedArtists(12143795131, 'mocolvin')
