from main import userPlayback
from flask import Flask ,render_template, request, redirect, url_for

app = Flask(__name__)

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
    return render_template('displayListeningHistory.html', tracks=tracks)