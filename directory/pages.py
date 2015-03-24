from flask import g
from directory import dbqueries
from placeList import PlaceList
import math
import sys

PLACES_PER_PAGE = 10

# TODO: consider using methods in Jinja template, object
def frontPage (title='Home', activity=None, county=None, page=1):
    placesList = getPlaceList(activity, county)
    numPlaces = placesList.length() / PLACES_PER_PAGE
    numPages = math.ceil (float(placesList.length()) / 
                                      PLACES_PER_PAGE)
    if (numPages > 1): 
      hasPages = True
    else:
      hasPages = False
    places = placesList.shorten_place_list(page, PLACES_PER_PAGE)
    return dict(title= title,
             activities= dbqueries.get_activities_list(),
             counties = dbqueries.get_counties_list(),
             activity = activity,
             county = county,
             page= page,
             numPlaces= numPlaces,
             numPages= numPages,
             hasPages= hasPages,
             places= places, 
             mapCenter= placesList.get_average_latlong(places))

class PlacePage:
    def __init__(self, place):
        self.activities =  dbqueries.get_activities_list()
        self.counties = dbqueries.get_counties_list()
        place_info = dbqueries.query_db(dbqueries.place_query, (place,), True)
        place_activities = [dict(name=row[0]) for row in 
                        dbqueries.query_db(dbqueries.place_activities, (place,))]
        if (place_info == None):
            self.name = "Not found"
            self.description = ""
        else:
            self.name = place_info[1]
            self.description = place_info[2]
            self.latitude = place_info[4]
            self.longitude = place_info[5]
            self.website = place_info[6]
            self.contact = place_info[7]
        if (place_activities == None):
            self.place_activities = ["None"]
        else: 
            self.place_activities = list(place_activities)
        self.title = place
        self.mapCenter = { 'latitude': self.latitude, 'longitude': self.longitude } 

def getPlaceList (activity=None, county=None):
    if (activity == None and county == None):
      cur = dbqueries.query_db(dbqueries.full_query)
      return PlaceList(cur)
    else:
        if (county == None):
            cur = dbqueries.query_db(dbqueries.query_join, (activity,))
            return PlaceList(cur)
        else:
            cur = dbqueries.query_db(dbqueries.county_query, (county,))
            return PlaceList(cur)

