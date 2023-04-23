#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """view function that displays all states currently in storage"""
    all_states = storage.all("State").values()
    return render_template('7-states_list.html', all_states=all_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """view function that displays all cities currently in storage"""
    all_states = storage.all("State").values()
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def teardown(self):
    """function that removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
