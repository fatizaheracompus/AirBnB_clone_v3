#!/usr/bin/python3
"""Flask apps that  generates completes html page containing location/amenity
dropdowne menu and rentale listing"""
from flask import Flask, render_template
from models import storage
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/1-hbnb')
def display_hbnb():
    """Generates page with popdown menu of the states/cities"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    cache_id = uuid.uuid4()
    return render_template('1-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close databases or the file storages"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
