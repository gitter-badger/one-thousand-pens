# This is some copy-pasta from the internet
# because the threading module was throwing errors
from gevent import monkey
monkey.patch_all()

from flask import Flask
from flask.ext.socketio import SocketIO, emit

from vote_manager import VoteManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PolarBearSunset'
socket = SocketIO(app)

vote_manager = VoteManager(socket)

@app.route('/')
def index():
    """
    Serves up our client to the user.
    """
    return app.send_static_file('index.html')


@socket.on('vote')
def add_vote(message):
    """
    When a vote event is emitted by the client we want to add
    that vote to our vote managers queue for it to handle.
    """
    word = message['word']
    vote_manager.queue.put(word)

def get_top_ten_words():
    pass

if __name__ == '__main__':
    socket.run(app)
