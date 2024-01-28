#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/hbnb')
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


if __name__ == '__main__':
    """Run the script"""
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
