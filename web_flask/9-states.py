#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import storage_t
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_list():
    """ Handles the state route to display a HTML page"""
    if storage_t == 'db':
        states = storage.all("State").values()
        sorted_states = sorted(states, key=lambda state: state.name)
        for state in sorted_states:
            state.cities = sorted(state.cities, key=lambda city: city.name)
    else:
        states = storage.all("State").values()
        sorted_states = sorted(states, key=lambda state: state.name)
        for state in sorted_states:
            state_cities = sorted_states.cities()
            state.cities = sorted(state_cities, key=lambda city: city.name)

    return render_template("7-states_list.html", states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_detail(state_id):
    """ Handles the state/<id> route to display a HTML page"""
    if storage_t == 'db':
        states = storage.all("State").values()
    else:
        states = storage.all("State").values()
        for state in states:
            state.cities = state.cities()
    state_by_city = None
    for state in states:
        if state.id == state_id:
            state_by_city = state
            state_by_city.cities = sorted(state.cities,
                                          key=lambda city: city.name)
            break

    return render_template("9-states.html", state=state_by_city)


@app.teardown_appcontext
def teardown_db(exception):
    """request to remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
