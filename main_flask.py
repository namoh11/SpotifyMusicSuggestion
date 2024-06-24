from main import userPlayback, userTopTracks, trackSuggestion, userTopArtists
from flask import Flask ,render_template, request, redirect, url_for, jsonify
import sys
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
# from flask_cors import CORS
load_dotenv()  # This loads the variables from the .env file into the environment
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')


app = Flask(__name__)
# CORS(app)

@app.route('/', methods = ['GET','POST'])
def menu():
    return render_template('menu.html')

@app.route('/listeninghistory', methods=['GET'])
def listening_history():
    return render_template('listeningHistory.html')

# @app.route('/listeninghistory', methods=['GET', 'POST'])
# def listening_history():
#     if request.method == 'POST':
#         numOfTracks = request.form['numOfTracks']
#         return redirect(url_for('displayListeningHistory', numOfTracks=numOfTracks))
#     return render_template('listeningHistory.html')

@app.route('/displayListeningHistory', methods=['GET'])
def display_listening_history():
    numOfTracks = request.args.get('numOfTracks', type=int)
    tracks = userPlayback(numOfTracks)
    return render_template('displayListeningHistory.html', tracks=tracks)#, jsonify(tracks)

@app.route('/toptracks', methods = ['GET'])
def top_tracks():
    return render_template('topTracks.html')

@app.route('/displaytoptracks', methods = ['GET'])
def display_top_tracks():
    numOfTracks = request.args.get('numOfTracks', type = int)
    time_range = request.args.get('time_range', type = str)
    tracks = userTopTracks(numOfTracks, time_range)
    return render_template('displayTopTracks.html', tracks = tracks)#, jsonify(tracks)

@app.route('/topartists', methods = ['GET'])
def top_artists():
    return render_template('topArtists.html')

@app.route('/displayTopArtists', methods = ['GET'])
def display_top_artists():
    numOfArtists = request.args.get('numOfArtists', type = int)
    time_range = request.args.get('time_range', type= str)
    artists = userTopArtists(numOfArtists, time_range)
    return render_template('displayTopArtists.html', artists = artists)

@app.route('/tracksuggestions', methods=['GET'])
def track_suggestion():
    return render_template('trackSuggestion.html')

@app.route('/displayTrackSuggestions', methods = ['GET'])
def display_track_suggestions():
    numOfTracks = request.args.get('numOfTracks', type= int)
    time_range = request.args.get('time_range', type= str)
    tracks = trackSuggestion(numOfTracks, time_range)
    return render_template('displayTrackSuggestions.html', tracks = tracks)#, jsonify(tracks)
