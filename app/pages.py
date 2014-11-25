from flask import g
from app import dbqueries
from placeList import PlaceList
import math

PLACES_PER_PAGE = 10

def frontPage (title='Home', activity=None, page=1):
    placesList = getPlaceList(activity)
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
             page= page,
             numPlaces= numPlaces,
             numPages= numPages,
             hasPages= hasPages,
             places= places, 
             mapCenter= placesList.get_average_latlong(places))
    
def getPlaceList (activity):
    if (activity == None):
      cur = dbqueries.query_db(dbqueries.full_query)
      return PlaceList(cur)
    else:
      cur = dbqueries.query_db(dbqueries.query_join, (activity,))
      return PlaceList(cur)
