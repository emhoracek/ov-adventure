from flask import render_template, g
from app import app
import os


def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def_query = ('select name, description from places ' + 
	     'order by name')

full_query = ('select places.name, places.description, ' +
	      'areas.name ' +
	      'FROM places JOIN areas ' +
	      'ON places.areaId = areas.id '
	      'order by places.name')

query_join = (' select places.name, places.description, areas.name '+
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

@app.route('/')
@app.route('/index')
def index():
	imageList = os.listdir('/home/libby/dev/outdoorRec/app/static/images/lrgImages')
	cur = query_db(full_query)
	places = [dict(name=row[0], 
		       description=row[1],
		       area=row[2]) for row in cur]
	return render_template('index.html', 
				title='Home',
				activities=get_activities_list(),
				places=places)

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
	places = [dict(name=row[0], 
		       description=row[1],
		       area=row[2]) for row in cur]
	return render_template('index.html',
			       title=activity,
			       activities=get_activities_list(),
			       places=places )	
