from flask import render_template, g
from app import app, pages, dbqueries, placeList
import os, math

@app.route('/')
@app.route('/index')
def index():
  thisPage = pages.frontPage('Home',None,1)
  return render_template('index.html',
          page=thisPage,
          places=thisPage['places'])

@app.route('/page')
@app.route('/page/<int:page>')
def page(page=1):
  thisPage = pages.frontPage('Page %s '% page, None, page)
  return render_template('index.html',
          page=thisPage,
          places=thisPage['places'])			        

@app.route('/places')
@app.route('/places/<place>')
def places(place=None):
	return render_template('index.html',
			       title=place,
			       activities=get_activities_list())

@app.route('/activities')
@app.route('/activities/<activity>')
def activity(activity=None):
  thisPage = pages.frontPage(activity, activity, 1)
  return render_template('index.html',
          page=thisPage,
          places=thisPage['places'])


				
