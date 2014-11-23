from flask import g
from app import dbqueries, placeList
import math

PLACES_PER_PAGE = 10

class FrontPage (object):
  def __init__(self, title='Home',
                     activity=None,
                     page=1):
    self.title=title
    self.activities = dbqueries.get_activities_list()
    self.placesList = self.getPlaceList(activity)
    self.page = page
    self.numPlaces = self.placesList.length() / PLACES_PER_PAGE
    self.numPages = math.ceil (float(self.placesList.length()) / 
                                      PLACES_PER_PAGE)
    if (self.numPages > 1): 
      self.hasPages = True
    else:
      self.hasPages = False
    self.places = self.placesList.shorten_place_list(page, PLACES_PER_PAGE)
    self.mapCenter = self.placesList.get_average_latlong(self.places)
    
  def getPlaceList (self, activity):
    if (activity == None):
      cur = dbqueries.query_db(dbqueries.full_query)
      return placeList.PlaceList(cur)
    else:
      cur = dbqueries.query_db(dbqueries.query_join, (activity,))
      return placeList.PlaceList(cur)
