# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.types import ARRAY
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
import datetime

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

# Done TODO: connect to a local postgresql database
migrate = Migrate(app, db)


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


class Shows(db.Model):
	__tablename__ = 'Shows'
	id = db.Column('id', db.Integer, primary_key=True)
	venue_id = db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'))
	artist_id = db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'))
	start_time = db.Column('start_time', db.DateTime)


class Venue(db.Model):
	__tablename__ = 'Venue'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	city = db.Column(db.String(120))
	state = db.Column(db.String(120))
	address = db.Column(db.String(120))
	genres = db.Column(ARRAY(db.String))
	phone = db.Column(db.Integer)
	image_link = db.Column(db.String(500))
	facebook_link = db.Column(db.String(120), )
	shows = db.relationship('Shows')


# TODO: implement any missing fields, as a database migration using Flask-Migrate


class Artist(db.Model):
	__tablename__ = 'Artist'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	city = db.Column(db.String(120))
	state = db.Column(db.String(120))
	phone = db.Column(db.Integer)
	genres = db.Column(ARRAY(db.String))
	image_link = db.Column(db.String(500))
	facebook_link = db.Column(db.String(120))
	seeking_talent = db.Column(db.Boolean())
	seeking_description = db.Column(db.Text())
	shows = db.relationship('Shows')


# TODO: implement any missing fields, as a database migration using Flask-Migrate

# Done: TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

# ----------------------------------------------------------------------------#
# Filters.
# ----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
	date = dateutil.parser.parse(value)
	if format == 'full':
		format = "EEEE MMMM, d, y 'at' h:mma"
	elif format == 'medium':
		format = "EE MM, dd, y h:mma"
	return babel.dates.format_datetime(date, format)


app.jinja_env.filters['datetime'] = format_datetime


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/')
def index():
	return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
	# Done: TODO: replace with real venues data.
	#       num_shows should be aggregated based on number of upcoming shows per venue.
	data = []
	all_cities = list(db.session.query(Venue.city, Venue.state).distinct().all())
	for city, state in all_cities:
		pcv = {"city": city, "state": state, "venues": []}
		per_city_venues = Venue.query.filter(Venue.city == city and Venue.state == state).all()
		for venue in per_city_venues:
			num_upcoming_show = len(Shows.query.filter( (Shows.venue_id==venue.id) | (Shows.start_time >
																						datetime.datetime.now())).all())
			pcv["venues"].append(
				{"id": venue.id, "name": venue.name, "num_upcoming_shows": num_upcoming_show})

		data.append(pcv)

	return render_template('pages/venues.html', areas=data);


@app.route('/venues/search', methods=['POST'])
def search_venues():
	# Done: TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
	# seach for Hop should return "The Musical Hop".
	# search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
	search_term = request.form.get('search_term')
	search_results = Venue.query.filter(Venue.name.ilike(f'%{search_term}%')).all()
	data = []
	for result in search_results:
		num_upcoming_show = len(Shows.query.filter((Shows.venue_id == result.id) | (Shows.start_time > datetime.datetime.now())).all())
		data.append({
			"id": result.id,
			"name": result.name,
			"num_upcoming_shows": num_upcoming_show,
		})
	response = {'count': len(search_results), 'data': data}

	return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
	# shows the venue page with the given venue_id
	# Done: TODO: replace with real venue data from the venues table, using venue_id
	venue_info = Venue.query.filter(Venue.id == venue_id).one().__dict__
	#data_past_shows = Shows.query.filter((Shows.venue_id==venue_id) | (Shows.start_time < datetime.datetime.now())).all()
	data_past_shows = Shows.query.join(Venue).filter(Shows.start_time<datetime.datetime.now()).all()
	past_shows = []
	for show in data_past_shows:
		artist = Artist.query.get(show.artist_id)
		past_shows.append({
			"artist_id": artist.id,
			"artist_name": artist.name,
			"artist_image_link": artist.image_link,
			"start_time": show.start_time
		})
	#data_upcoming_shows = Shows.query.filter( (Shows.venue_id==venue_id) | (Shows.start_time > datetime.datetime.now())).all()
	data_upcoming_shows = Shows.query.join(Venue).filter(Shows.start_time > datetime.datetime.now()).all()

	upcoming_shows = []
	for show in data_upcoming_shows:
		artist = Artist.query.get(show.artist_id)
		past_shows.append({
			"artist_id": artist.id,
			"artist_name": artist.name,
			"artist_image_link": artist.image_link,
			"start_time": show.start_time
		})
	past_shows_count = len(data_past_shows)
	upcoming_shows_count = len(data_upcoming_shows)
	venue_info["upcoming_shows", "past_shows", "upcoming_shows_count", "past_shows_count"] = upcoming_shows, past_shows, \
																				upcoming_shows_count, past_shows_count


	return render_template('pages/show_venue.html', venue=venue_info)


#  Create Venue
#  ----------------------------------------------------------------


@app.route('/venues/create', methods=['GET'])
def create_venue_form():
	form = VenueForm()
	return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
	# Done TODO: insert form data as a new Venue record in the db, instead
	# Done TODO: modify data to be the data object returned from db insertion
	new_venue = request.form.to_dict()
	try:
		venue = Venue(**new_venue)
		db.session.add(venue)
		db.session.commit()
		# on successful db insert, flash success
		flash('Venue ' + request.form['name'] + ' was successfully listed!')

	# Done: TODO: on unsuccessful db insert, flash an error instead.
	# e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
	# see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
	except Exception as e:
		flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.' + str(e))
		db.session.rollback()
	finally:
		db.session.close()

	return render_template('pages/home.html')


@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
	# Done: TODO: Complete this endpoint for taking a venue_id, and using
	# SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
	try:
		todo = Venue.query.get(venue_id)
		db.session.delete(todo)
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()

	# BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
	# clicking that button delete it from the db then redirect the user to the homepage
	return None


#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
	# Done: TODO: replace with real data returned from querying the database
	all_artists = Artist.query.all()
	data = []
	for artist in all_artists:
		data.append(artist.__dict__)

	return render_template('pages/artists.html', artists=data)


@app.route('/artists/search', methods=['POST'])
def search_artists():
	# Done: TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
	# search for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
	# search for "band" should return "The Wild Sax Band".
	search_term = request.form.get('search_term')
	search_results = Artist.query.filter(Artist.name.ilike(f'%{search_term}%')).all()
	data = []
	for result in search_results:
		num_upcoming_shows = len(Shows.query.filter((Shows.artist_id == result.id) | (Shows.start_time >
		                                                                              datetime.datetime.now())).all())
		data.append({
			"id": result.id,
			"name": result.name,
			"num_upcoming_shows": num_upcoming_shows,
		})
	response = {'count': len(search_results), 'data': data}

	return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
	# shows the venue page with the given venue_id
	# Done: TODO: replace with real venue data from the venues table, using venue_id
	artist_info = Artist.query.filter(Artist.id == artist_id).one().__dict__
	artist_info['genres'] = ["Alternative"]
	# data_past_shows = Shows.query.filter(
	# 	(Shows.artist_id == artist_id) | (Shows.start_time < datetime.datetime.now())).all()
	data_past_shows = Shows.query.join(Artist).filter(Shows.start_time < datetime.datetime.now()).all()
	past_shows = []
	for show in data_past_shows:
		venue = Venue.query.get(show.venue_id)
		past_shows.append({
			"venue_id": venue.id,
			"venue_name": venue.name,
			"venue_image_link": venue.image_link,
			"start_time": show.start_time
		})
	# data_upcoming_shows = Shows.query.filter(
	# 	(Shows.artist_id == artist_id) | (Shows.start_time > datetime.datetime.now())).all()
	data_upcoming_shows = Shows.query.join(Artist).filter(Shows.start_time > datetime.datetime.now()).all()
	upcoming_shows = []
	for show in data_upcoming_shows:
		venue = Venue.query.get(show.venue_id)
		upcoming_shows.append({
			"venue_id": venue.id,
			"venue_name": venue.name,
			"venue_image_link": venue.image_link,
			"start_time": show.start_time
		})
	past_shows_count = len(data_past_shows)
	upcoming_shows_count = len(data_upcoming_shows)
	artist_info["upcoming_shows"] = upcoming_shows
	artist_info["past_shows"] = past_shows
	artist_info["upcoming_shows_count"] = upcoming_shows_count
	artist_info["past_shows_count"] = past_shows_count

	return render_template('pages/show_artist.html', artist=artist_info)


#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
	form = ArtistForm()
	# Done: TODO: populate form with fields from artist with ID <artist_id>
	artist = Artist.query.get(artist_id)
	return render_template('forms/edit_artist.html', form=form, artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
	# Done: TODO: take values from the form submitted, and update existing
	# artist record with ID <artist_id> using the new attributes
	artist = Artist.query.get(artist_id)
	new_data = request.form.to_dict()
	try:
		for fname, fvalue in new_data.items():
			setattr(artist, fname, fvalue)
		db.session.commit()
	except Exception as e:
		db.session.rollback()
		flash("Can not edit, Error: ", e)
	finally:
		db.session.close()

	return redirect(url_for('show_artist', artist_id=artist_id))


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
	form = VenueForm()
	# Done: TODO: populate form with values from venue with ID <venue_id>
	venue = Venue.query.get(venue_id)
	return render_template('forms/edit_venue.html', form=form, venue=venue)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
	# Done: TODO: take values from the form submitted, and update existing
	# venue record with ID <venue_id> using the new attributes
	venue = Venue.query.get(venue_id)
	new_data = request.form.to_dict()
	try:
		for fname, fvalue in new_data.items():
			setattr(venue, fname, fvalue)
		db.session.commit()
	except Exception as e:
		db.session.rollback()
		flash("Can not edit, Error: ", e)
	finally:
		db.session.close()
	return redirect(url_for('show_venue', venue_id=venue_id))


#  Create Artist
#  ----------------------------------------------------------------


@app.route('/artists/create', methods=['GET'])
def create_artist_form():
	form = ArtistForm()
	return render_template('forms/new_artist.html', form=form)


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
	# called upon submitting the new artist listing form
	# Done: TODO: insert form data as a new Venue record in the db, instead
	# Done: TODO: modify data to be the data object returned from db insertion
	new_artist = request.form.to_dict()
	seeking_talent = new_artist['seeking_talent']
	seeking_boolean = True if seeking_talent=='y' else False
	new_artist['seeking_talent'] = seeking_boolean
	new_artist['genres'] = request.form.getlist('genres')
	try:
		artist = Artist(**new_artist)
		db.session.add(artist)
		db.session.commit()
		# Done: TODO: on unsuccessful db insert, flash an error instead.
		# e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
		# on successful db insert, flash success
		flash('Artist ' + request.form['name'] + ' was successfully Added!')

	except Exception as e:
		flash('An error occurred. Artist ' + request.form['name'] + ' could not be Added.' + str(e))
		db.session.rollback()
	finally:
		db.session.close()

	return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
	# displays list of shows at /shows
	# Done: TODO: replace with real venues data.
	#       num_shows should be aggregated based on number of upcoming shows per venue.
	current_time = datetime.datetime.now()
	all_shows = Shows.query.filter(Shows.start_time > current_time).order_by(Shows.venue_id).all()
	data = []
	for show in all_shows:
		venue = Venue.query.get(show.venue_id)
		artist = Artist.query.get(show.artist_id)
		data.append({
			"venue_id": venue.id,
			"venue_name": venue.name,
			"artist_id": artist.id,
			"artist_name":artist.name,
			"artist_image_link": artist.image_link,
			"start_time": show.start_time
		})

	return render_template('pages/shows.html', shows=data)


@app.route('/shows/create')
def create_shows():
	# renders form. do not touch.
	form = ShowForm()
	return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
	# called to create new shows in the db, upon submitting new show listing form
	# Done: TODO: insert form data as a new Show record in the db, instead
	new_show = request.form.to_dict()
	try:
		# To check whether specific venue and artist exist of not
		Venue.query.get(new_show['venue_id'])
		Artist.query.get(new_show['artist_id'])

		shows_table_instance = Shows()
		shows_table_instance.artist_id = new_show['artist_id']
		shows_table_instance.venue_id = new_show['venue_id']
		shows_table_instance.start_time = new_show['start_time']
		db.session.add(shows_table_instance)
		db.session.commit()
		# on successful db insert, flash success
		flash('Show was successfully listed!')
	# Done: TODO: on unsuccessful db insert, flash an error instead.
	except Exception as e:
		flash('An error occurred. Show could not be listed.' + str(e))
		db.session.rollback()
	finally:
		db.session.close()

	return render_template('pages/home.html')


@app.errorhandler(404)
def not_found_error(error):
	return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
	return render_template('errors/500.html'), 500


if not app.debug:
	file_handler = FileHandler('error.log')
	file_handler.setFormatter(
		Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
	)
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('errors')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
	app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
