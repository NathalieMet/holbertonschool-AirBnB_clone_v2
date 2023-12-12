#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
from markupsafe import escape
from models.state import State
from models.city import City


app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states)

@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

if __name__ == '__main__':
    # Run the application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
