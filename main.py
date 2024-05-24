import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys

'''shows top artists for myself, in 3 different time ranges
'''
# topArtistsAndTrackScope = 'user-top-read'
#playbackScope = 'user-read-recently-played'
# ranges = ['short_term', 'medium_term', 'long_term']

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=topArtistsAndTrackScope))
# print('Top artists:/n')
# for sp_range in ['short_term', 'medium_term', 'long_term']:
#     print("range:", sp_range)

#     results = sp.current_user_top_artists(time_range=sp_range, limit=50)

#     for i, item in enumerate(results['items']):
#         print(i, item['name'])
#     print()
# print playback
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=playbackScope)) 
# results = sp.current_user_recently_played(limit=50, after=None, before=None)
# print('Recent Listening')
# results = sp.current_user_recently_played(limit=20, after=None)
# for i, item in enumerate(results['items']):
#     #print(i, item['track']['name']['artist'])
#     # vs
#      print(i, item['track']['name'], "-", item['track']['artists'][0]['name'])

def menu():
    print("Welcome to this spotify thing.\nPress 1 to see your track listening history\nPress 2 to see your top tracks.\nPress x to quit. ") 
    userInput = getUserInput()
    if userInput == '1':
        numOfTracks = int(input("How many tracks do you want to see? "))
        if checkNumberOfTracks(numOfTracks) == True:
            userPlayback(numOfTracks)
        else:
            print("Number of tracks must be at least 1, but cannot exceed 50.\n\n")
            menu()

    if userInput == '2':
        numOfTracks = int(input("How many tracks do you want to see? "))
        if checkNumberOfTracks(numOfTracks):
            userTopTracks(numOfTracks)
        else:
            print("Number of tracks must be at least 1, but cannot exceed 50.\n\n")
            menu()
    if userInput == 'x':
        sys.exit("Goodbye!")

def checkNumberOfTracks(numOfTracks):
    validNumber = True
    if ((numOfTracks <= 0) or (numOfTracks > 50)):
        #print("Number of tracks must be at least 1, but cannot exceed 50.")
        validNumber = False
    return validNumber
def getUserInput():
    userInput = input()
    return userInput

def userPlayback(numOfTracks):
    authorizationScope = 'user-read-recently-played'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=authorizationScope))
    print('Your ' + str(numOfTracks) + ' last listened to tracks: ') # direct cast of track number to a string to concatenate it
    results = sp.current_user_recently_played(limit=numOfTracks, after=None)
    for i, item in enumerate(results['items']):
     print(i + 1, item['track']['name'], "-", item['track']['artists'][0]['name'])

def userTopTracks(numOfTracks):
    authorizationScope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager= SpotifyOAuth(scope=authorizationScope))
    print("Select 1 for the last 4 weeks, 2 for the last 6 months, and 3 for all-time listening")
    userInput = getUserInput()
    if userInput == '1':
        print("Top tracks of the last 4 weeks: ")
        results = sp.current_user_top_tracks(time_range='short_term', limit=numOfTracks)
        for i, item in enumerate(results['items']):
            print(i + 1, item['name'], "-", item['artists'][0]['name'])
    elif userInput == '2':
        print("Top tracks of the last 6 months: ")
        results = sp.current_user_top_tracks(time_range='medium_term', limit=numOfTracks)
        for i, item in enumerate(results['items']):
            print(i + 1, item['name'], "-", item['artists'][0]['name'])
    elif userInput == '3':
        print("Top tracks of all time: ")
        results = sp.current_user_top_tracks(time_range='long_term', limit=numOfTracks)
        for i, item in enumerate(results['items']):
            print(i + 1, item['name'], "-", item['artists'][0]['name'])





def main():
    menu()

if __name__ == "__main__":
    main()
'''
shows led zeppelin audio samples and cover art for top ten tracks
'''
# from spotipy.oauth2 import SpotifyClientCredentials
# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.artist_top_tracks(lz_uri)

# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()