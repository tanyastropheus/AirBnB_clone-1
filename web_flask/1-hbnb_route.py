#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
        return 'HBNB'

if __name__ == '__main__':
        # app.run() defaults to listening on port 5000
        app.run(host="0.0.0.0")
