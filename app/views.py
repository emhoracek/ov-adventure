from flask import render_template, g
from app import app
import os, math

PLACES_PER_PAGE = 10

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def_query = ('select name, description from places ' + 
	     'order by name')

full_query = ('select places.name, places.description, ' +
	      'areas.name, places.latitude, places.longitude ' +
	      'FROM places JOIN areas ' +
	      'ON places.areaId = areas.id '
	      'order by places.name')

query_join = (' select places.name, places.description, areas.name, '+
	      ' places.latitude, places.longitude ' +
	      ' FROM places, areas JOIN joinActPlace, activities ' +
	      ' ON places.id = joinActPlace.placeId AND ' +
	      ' activities.id = joinActPlace.activityId ' +  
	      ' where activities.name = ? AND areas.id = places.areaId')

query_activities = ('select places.name, places.description, areas.name ' +
		   'FROM places JOIN ? as "a" ' +
		   'ON places.id = a.placeId ' +
		   'order by places.name')

def get_activities_list():
	cur = query_db('select name from activities order by name')
	return [dict(name=row[0]) for row in cur]

def get_average_latlong(listplaces):
	total_latitude = 0
	total_longitude = 0
	average_latitude = 0
	average_longitude = 0
	for place in listplaces:
		total_latitude = place['latitude'] + total_latitude
		total_longitude = place['longitude'] + total_longitude
	average_latitude = total_latitude/len(listplaces)
	average_longitude = total_longitude/len(listplaces)
	return { 'latitude': average_latitude,
		 'longitude': average_longitude }

def get_place_list():
	cur = query_db(full_query)
	places = [dict(name=row[0], 
		       description=row[1],
		       area=row[2],
		       latitude=row[3],
		       longitude=row[4]) for row in cur]
	return places

def shorten_place_list(places, page):
	maxPlaces = page * PLACES_PER_PAGE
	startPlace = maxPlaces - PLACES_PER_PAGE
	places = places[startPlace : maxPlaces]
	return places

@app.route('/')
@app.route('/index')
def index():
	imageList = os.listdir('/home/libby/dev/outdoorRec/app/static/images/lrgImages')
	placesList = get_place_list()
	numPlaces = (len (placesList) / PLACES_PER_PAGE)
	numPages = math.ceil (float(len(placesList)) / PLACES_PER_PAGE)
	hasPages = False
	if (numPages > 1):
		hasPages = True
	places = shorten_place_list(placesList, 1)
	return render_template('index.html', 
				title='Home',
				activities=get_activities_list(),
				places=places,
				numPlaces = numPlaces,
				hasPages=hasPages,
				numPages= (math.floor (numPages)),
				map_center = get_average_latlong(places) )

@app.route('/page')
@app.route('/page/<page>')
def page(page=1):
	page = int(page)
	placesList = get_place_list()
	places = shorten_place_list(placesList, page)
	numPages = math.ceil (float(len(placesList))/ PLACES_PER_PAGE)
	hasPages = False
	if (numPages > 1):
		hasPages = True
	return render_template('index.html',
			       activities=get_activities_list(),
			       places=places,
			       page=page,
			       numPages = numPages,
			       map_center = get_average_latlong(places)
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
	cur = query_db(query_join, (activity,))
	placesList = [dict(name=row[0], 
		       description=row[1],
		       area=row[2],
		       latitude=row[3],
		       longitude=row[4]) for row in cur]
	places = shorten_place_list(placesList, 1)
	numPages = math.ceil (float(len(placesList))/ PLACES_PER_PAGE)
	hasPages = False
	if (numPages > 1):
		hasPages = True
	return render_template('index.html',
			       title=activity,
			       activities=get_activities_list(),
			       activity=activity,
			       places=places,
			       page=page,
			       numPages = numPages,
			       map_center = get_average_latlong(places))
