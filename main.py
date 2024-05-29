import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
def menu():
    print("Welcome to this spotify thing.\nPress 1 to see your track listening history\nPress 2 to see your top tracks.\nPress 3 to see recommended music.\nPress x to quit. ") 
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
    if userInput == '3':
        numOfTracks = int(input("How many tracks do you want to see? "))
        if checkNumberOfTracks(numOfTracks):
            trackSuggestion(numOfTracks)
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
    print("Returning to menu...\n\n") 
    menu()

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
    print("Returning to menu...\n\n") 
    menu()

def trackSuggestion(numOfTracks): # can actually provide 100 recommendations NOT 50, be sure to handle that 
    authorizationScope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager= SpotifyOAuth(scope=authorizationScope))
    print('Recommendations are based off your past listening history. What scope of time do you want your recommendations to be based off of?')
    print("Select 1 for the last 4 weeks, 2 for the last 6 months, and 3 for all-time.")
    userInput = getUserInput()
    if userInput == '1':
        timeRange = 'short_term'
    elif userInput == '2':
        timeRange = 'medium_term'
    elif userInput == '3':
        timeRange = 'long_term'
    
    trackURIList = []
    print(timeRange)
    # generate results
    results = sp.current_user_top_tracks(time_range = timeRange,limit= numOfTracks)
    # iterate through every(?) track and pull only the track uri,
    for item in results['items']:
        # add uri to trackURIList
        trackURIList.append(item['uri'])
    print(trackURIList)
    # call recommendations(seed_tracks = trackURIList, limit= numOfTracks) 
    recommendedSongs = sp.recommendations(seed_tracks=trackURIList, limit= numOfTracks) 
    #print(recommendedSongs)
    # for i, item in enumerate(recommendedSongs['items']):
    #     print(i + 1, item['track']['name'], "-", item['track']['artists'][0]['name'])
    # for i, item in enumerate(recommendedSongs.get('tracks', [])):
    #     track_name = item.get('name', 'Unknown Track')
    #     artist_name = item['artists'][0]['name'] if item.get('artists') else 'Unknown Artist'
    #     print(f"{i + 1}: {track_name} - {artist_name}")
    for i, item in enumerate(recommendedSongs['tracks']):
            print(i + 1, item['name'], "-", item['artists'][0]['name'])
    print("Returning to menu...\n\n") 
    menu()


def main():
    menu()

if __name__ == "__main__":
    main()