from flask import g

# This module contains the functions for querying the database

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

query_activities = ('select places.name, places.description, counties.name ' +
		    'FROM places JOIN ? as "a" ' +
		    'ON places.id = a.placeId ' +
		    'order by places.name')

def get_activities_list():
	cur = query_db('select name from activities order by name')
	return [row[0] for row in cur]

def get_counties_list():
        cur = query_db('select name from counties order by name')
        return [row[0] for row in cur]
    
full_query = ('select places.name, places.description, ' +
	      'counties.name, places.latitude, places.longitude ' +
	      'FROM places JOIN counties ' +
	      'ON places.countyId = counties.id '
	      'order by places.name')

def superQuery (selected):
    all_counties = get_counties_list()
    all_activities = get_activities_list()
    activities = []
    counties = []
    for selection in selected:
        if selection in all_counties:
            counties.append(selection)
        if selection in all_activities:
            activities.append(selection)
    longquery = ( '' +
            'SELECT places.name, places.description, counties.name, ' + 
            'places.latitude, places.longitude, GROUP_CONCAT(activities.name) ' + 
            'FROM counties, places LEFT JOIN joinActPlace LEFT JOIN activities ' +
            'ON places.id = joinActPlace.placeId AND ' +
            'activities.id = joinActPlace.activityId ' +
            'WHERE places.countyId = counties.id ' + 
            'GROUP BY places.id')
    cur = query_db(longquery)
    places = [dict(name=row[0],
                 description = row[1],
                 area = row[2],
                 latitude = row[3],
                 longitude = row[4],
                 actList = row[5]) for row in cur ]
    if counties != []:
        places = [row for row in places if row['area'] in counties]
    def f(d):
        if activities == []:
            return True
        if d['actList'] is None:
            return False
        return set(d['actList'].split(',')).issuperset(activities)
    return filter(f, places)

county_query = ('select places.name, places.description, ' +
	      'counties.name, places.latitude, places.longitude ' +
	      'FROM places JOIN counties ' +
	      'ON places.countyId = counties.id ' +
              'where counties.name = ? ' +
	      'order by places.name')

place_query = ('SELECT * FROM places WHERE name = ?')

place_activities = ('SELECT activities.name FROM activities ' + 
                    'JOIN joinActPlace, places ' + 
                    'ON places.id = joinActPlace.placeId ' +
                    'AND activities.id = joinActPlace.activityId ' +
                    'WHERE places.name = ? ORDER BY activities.name')
