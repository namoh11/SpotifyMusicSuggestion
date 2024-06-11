import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
from dotenv import load_dotenv
import os
import random

load_dotenv()  # This loads the variables from the .env file into the environment
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

def menu():
    print("Welcome to this spotify thing.\nPress 1 to see your track listening history\nPress 2 to see your top tracks.\nPress 3 to see recommended music.\nPress x to quit. ") 
    userInput = getUserInput()
    if userInput == '1':
        numOfTracks = input("How many tracks do you want to see? ")

        # check for a valid selected num of tracks 0 <= 50
        if checkNumberOfTracks(numOfTracks) == True:
            userPlayback(numOfTracks)
        else:
            # print("Number of tracks must be at least 1, but cannot exceed 50.\n\n")
            menu()

    if userInput == '2':
        numOfTracks = (input("How many tracks do you want to see? "))
        if checkNumberOfTracks(numOfTracks):
            userTopTracks(numOfTracks)
        else:
            # print("Number of tracks must be at least 1, but cannot exceed 50.\n\n")
            menu()

    if userInput == '3':
        numOfTracks = (input("How many tracks do you want to see? "))
        if checkNumberOfTracks(numOfTracks):
            trackSuggestion(numOfTracks)
        else:
            # print("Number of tracks must be at least 1, but cannot exceed 50.\n\n")
            menu()

    if userInput == 'x':
        sys.exit("Goodbye!")


def checkNumberOfTracks(numOfTracks):
    '''Check and sanitize user input for an int value, validate int is between 0 and 50.'''
    if type(numOfTracks) is not int:
        try: # convert into int, return False otherwise
            numOfTracks = int(numOfTracks)
        except(ValueError):
            print("Your input is not an integer.\n\n")
            return False

    if ((numOfTracks <= 0) or (numOfTracks > 50)):
        print("Number of tracks must be at least 1, but cannot exceed 50.\n\n")
        return False
    return True

def getUserInput():
    userInput = input()
    return userInput

'''
User Playback
inputs: 
    numOfTracks: represents number of songs a user can read of their past listening history
    - can only return between 1 and 50 tracks
return:
    trackDetails: a list of details about a track. included info is order number, title, artist name
'''
def userPlayback(numOfTracks):
    authorizationScope = 'user-read-recently-played'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=authorizationScope))
    print('Your ' + str(numOfTracks) + ' last listened to tracks: ') # direct cast of track number to a string to concatenate it
    results = sp.current_user_recently_played(limit=numOfTracks, after=None)
    trackDetails = []
    for i, item in enumerate(results['items']):
        trackDetails.append({
            'track_number': i + 1,
            'track_name': item['track']['name'],
            'artist_name': item['track']['artists'][0]['name']
        })
    return trackDetails

'''
User Top Tracks
inputs:
    numOfTracks: numOfTracks: represents number of songs a user can read of their past listening history
    - can only return between 1 and 50 tracks
return:
    track
'''
def userTopTracks(numOfTracks, time_range):
    authorizationScope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=authorizationScope))

    if time_range == 'Short Term':
        results = sp.current_user_top_tracks(time_range='short_term', limit=numOfTracks)
    elif time_range == 'Past 6 months':
        results = sp.current_user_top_tracks(time_range='medium_term', limit=numOfTracks)
    elif time_range == 'All time':
        results = sp.current_user_top_tracks(time_range='long_term', limit=numOfTracks)
    else:
        return []  # Return an empty list if the time_range is invalid

    trackDetails = []
    for i, item in enumerate(results['items']):
        trackDetails.append({
            'track_number': i + 1,
            'track_name': item['name'],
            'artist_name': item['artists'][0]['name']
        })
    return trackDetails

def trackSuggestion(numOfTracks, time_range):
    authorizationScope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=authorizationScope))
    
    if time_range == 'Short Term':
        results = sp.current_user_top_tracks(time_range='short_term', limit=numOfTracks)
    elif time_range == 'Past 6 months':
        results = sp.current_user_top_tracks(time_range='medium_term', limit=numOfTracks)
    elif time_range == 'All time':
        results = sp.current_user_top_tracks(time_range='long_term', limit=numOfTracks)
    else:
        return []  # Return an empty list if the time_range is invalid

    trackURIList = []
    revisedTrackURIList = []

    for item in results['items']:
        trackURIList.append(item['uri'])

    randomURI = random.sample(trackURIList, min(5, len(trackURIList)))
    revisedTrackURIList.extend(randomURI)

    recommendedSongs = sp.recommendations(seed_tracks=revisedTrackURIList, limit=numOfTracks)

    trackDetails = []
    for i, item in enumerate(recommendedSongs['tracks']):
        trackDetails.append({
            'track_number': i + 1,
            'track_name': item['name'],
            'artist_name': item['artists'][0]['name']
        })
    return trackDetails

def main():
    menu()

if __name__ == "__main__":
    main()