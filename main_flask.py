from flask import Flask ,render_template
app = Flask(__name__)
@app.route('/', methods = ['GET','POST'])
def menu():
    return render_template('menu.html')

@app.route('/trackhistory', methods = ['POST'])
def trackHistory():
    numOfTracks = request.args.get('numOfTracks')
    numOfTracks = int(numOfTracks)
    # how do i print out the dictionary of songs without printing a dictionary lmaooo
    return render_template('listeningHistory.html')