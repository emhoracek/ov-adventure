from flask import g
from directory import dbqueries, app
from placeList import PlaceList
import math
import sys
from os import listdir


PLACES_PER_PAGE = 10

# TODO: consider using methods in Jinja template, object
def frontPage (title='Home', selected=[], page=1):
    placesList = PlaceList(selected)
    numPlaces = placesList.length() / PLACES_PER_PAGE
    numPages = math.ceil (float(placesList.length()) / 
                                      PLACES_PER_PAGE)
    if (numPages > 1): 
      hasPages = True
    else:
      hasPages = False
    activities= dbqueries.get_activities_list()
    counties = dbqueries.get_counties_list()
    selected_activities = [s for s in selected if s in activities]
    selected_counties = [s for s in selected if s in counties]
    places = placesList.shorten_place_list(page, PLACES_PER_PAGE)
    return dict(title= title,
             activities = activities,
             counties = counties,
             selected = selected,
             selected_counties = selected_counties,
             selected_activities = selected_activities,
             numPlaces= numPlaces,
             numPages= numPages,
             hasPages= hasPages,
             TILE_SERVER = app.config['TILE_SERVER'],
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
        self.images = [image for image in listdir(app.config['PHOTOS']) 
                        if image.startswith(self.name)]
        print self.images
        self.title = place
        self.args = []
        self.tiles = app.config['TILE_SERVER']
        self.mapCenter = { 'latitude': self.latitude, 'longitude': self.longitude } 

