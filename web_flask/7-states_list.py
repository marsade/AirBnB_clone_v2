#!/usr/bin/python3
"""Starts a Flask appplication"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route('/states_list')
def list_states():
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """Run the appplication"""
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
