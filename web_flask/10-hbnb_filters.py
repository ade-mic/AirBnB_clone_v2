#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import storage_t
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def state_list():
    """ Handles the state route to display a HTML page"""
    if storage_t == 'db':
        states = storage.all("State").values()
        sorted_states = sorted(states, key=lambda state: state.name)
        for state in sorted_states:
            state.cities = sorted(state.cities, key=lambda city: city.name)
        amenities = storage.all("Amenity").values()
        amenities = sorted(amenities, key=lambda amenity: amenity.name)

    return render_template("10-hbnb_filters.html", states=sorted_states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """request to remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
