#!/usr/bin/python3
from flask import Flask
import string
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
        return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
        return 'C %s' % text.replace('_', ' ')

if __name__ == '__main__':
        # app.run() defaults to listening on port 5000
        app.run(host="0.0.0.0")
