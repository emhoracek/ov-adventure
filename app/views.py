from flask import render_template, g
from app import app, dbqueries, placeList
import os, math

PLACES_PER_PAGE = 10

@app.route('/')
@app.route('/index')
def index():
	cur = dbqueries.query_db(dbqueries.full_query)
	placesList = placeList.PlaceList(cur)
	numPlaces = placesList.length() / PLACES_PER_PAGE
	numPages = math.ceil (float(placesList.length()) / PLACES_PER_PAGE)
	hasPages = False
	if (numPages > 1):
		hasPages = True
	places = placesList.shorten_place_list(1, PLACES_PER_PAGE)
	return render_template('index.html', 
				title='Home',
				activities=dbqueries.get_activities_list(),
				places=places,
				page=1,
				numPlaces = numPlaces,
				hasPages=hasPages,
				numPages= (math.floor (numPages)),
				map_center = placesList.get_average_latlong() )

@app.route('/page')
@app.route('/page/<int:page>')
def page(page=1):
	cur = dbqueries.query_db(dbqueries.full_query)
	placesList = placeList.PlaceList(cur)
	numPlaces = placesList.length() / PLACES_PER_PAGE
	numPages = math.ceil (float(placesList.length()) / PLACES_PER_PAGE)
	hasPages = False
	if (numPages > 1):
		hasPages = True
	places = placesList.shorten_place_list(page, PLACES_PER_PAGE)
	return render_template('index.html',
			       activities=dbqueries.get_activities_list(),
			       places=places,
			       page=page,
			       numPages = numPages,
			       hasPages=hasPages,
			       map_center = placesList.get_average_latlong()
			       )			        

@app.route('/places')
@app.route('/places/<place>')
def places(place=None):
	return render_template('index.html',
			       title=place,
			       activities=get_activities_list())

@app.route('/activities')
@app.route('/activities/<activity>')
def activity(activity=None):
	cur = dbqueries.query_db(dbqueries.query_join, (activity,))	
	placesList = placeList.PlaceList(cur)
	numPlaces = placesList.length() / PLACES_PER_PAGE
	numPages = math.ceil (float(placesList.length()) / PLACES_PER_PAGE)
	hasPages = False
	if (numPages > 1):
		hasPages = True
	places = placesList.shorten_place_list(1, PLACES_PER_PAGE)
	return render_template('index.html',
			       title=activity,
			       activities=dbqueries.get_activities_list(),
			       activity=activity,
			       places=places,
			       page=page,
			       numPages = numPages,
			       map_center = placesList.get_average_latlong()
				)
