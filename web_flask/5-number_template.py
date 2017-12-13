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
def c_text(text):
        return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
def python():
        return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
        return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
        return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
        return render_template('5-number.html', num=n)


if __name__ == '__main__':
        # app.run() defaults to listening on port 5000
        app.run(host="0.0.0.0")
