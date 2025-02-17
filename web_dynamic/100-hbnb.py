#!/usr/bin/python3
"""Flask apps to generates completes html page containing location/amenity
dropdown menu and the rental listing"""
from flask import Flask, render_template
from models import storage
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/100-hbnb')
def display_hbnb():
    """Generates page with popdown menus of the states/cities"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    cache_id = uuid.uuid4()
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Closes databases or the file storages"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
