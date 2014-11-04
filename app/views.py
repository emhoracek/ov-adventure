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
	      ' areas.name ' +
	      'FROM places JOIN areas ' +
	      'ON places.areaId = areas.id '
	      'order by places.name')

activity_list = ('select name from activities order by name')

query_join = (' select joinActPlace.placeId '+
	      ' FROM activities JOIN joinActPlace ' +
	      ' ON activities.id = joinActPlace.activityId' +  
	      ' where activities.name = "?"')

query_activities = ('select places.name, places.description, areas.name ' +
		   'FROM places JOIN (?) as "a" ' +
		   'ON places.id = a.placeId ' +
		   'order by places.name')

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Jesse' }
	imageList = os.listdir('/home/libby/dev/outdoorRec/app/static/images/lrgImages')
	cur = query_db(full_query)
	places = [dict(name=row[0], 
		       description=row[1],
		       area=row[2]) for row in cur]
	cur = query_db(activity_list)
	activities = [dict(name=row[0]) for row in cur]
	return render_template('index.html', 
				title='Home',
				activities=activities,
				user=user,
				places=places)

@app.route('/places')
@app.route('/places/<place>')
def places(place=None):
	return render_template('index.html')

@app.route('/activities')
@app.route('/activities/<activity>')
def activity(activity=None):
	cur = query_db(query_join, (activity,))
	cur = query_db(query_activities, (cur,))
	places = [dict(name=row[0], 
		       description=row[1],
		       area=row[2]) for row in cur]
	return render_template('index.html',
			       title=activity,
			       places=places )	
