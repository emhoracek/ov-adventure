from flask import render_template, g, request, session, flash, redirect, url_for, abort
from directory import app
import pages, dbinserts, placeList, users
import os, math
import dbqueries

@app.route('/')
@app.route('/index')
def index():
  thisPage = pages.frontPage()
  return render_template('index.html',
          page=thisPage,
          places=thisPage['places'])

@app.route('/page')
@app.route('/page/<int:page>')
def page(page=1):
  thisPage = pages.frontPage('Page %s '% page, None, None, page)
  return render_template('index.html',
          page=thisPage,
          places=thisPage['places'])			        

@app.route('/places')
@app.route('/places/<place>')
def places(place=None):
  thisPage = pages.PlacePage(place)
  print("Hello")
  return render_template('place.html',
			  page=thisPage)

@app.route('/tags/<searchargs>')
def tags(tags=None):
    params = search-args.split('&')
    # params is a list of stuff like ['county=Ohio', 'activity=running']
    # convert list to dict of (country||activity: value)
    thisPage = pages.frontPage()
    return render_template('index.html',
                           page=thisPage)

@app.route('/activities')
@app.route('/activities/<activity>')
def activity(activity=None):
  thisPage = pages.frontPage(activity, activity, None, 1)
  return render_template('index.html',
          page=thisPage,
          places=thisPage['places'])

@app.route('/counties')
@app.route('/counties/<county>')
def county(county=None):
    thisPage = pages.frontPage(county, None, county, 1)
    return render_template('index.html',
                           page=thisPage,
                           places=thisPage['places'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    thisPage = pages.frontPage()
    error = None
    import dbqueries
    if request.method == 'POST':
        db_user = dbqueries.query_db(
            "select username, password FROM users WHERE username = ?", (request.form['username'],), True)
        admin_user = users.User("admin", db_user[1])
        if request.form['username'] != "admin":
            error = 'Invalid username'
        elif admin_user.check_password(request.form['password']):
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error,
                           page=thisPage)

@app.route('/add')
def add():
  if not session.get('logged_in'):
        abort(401)
  thisPage = pages.frontPage()
  return render_template('add.html',
            page=thisPage )

@app.route('/new', methods=['POST'])
def new():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute(dbinserts.add_new_place,
                 [ request.form['name'], 
                   request.form['description'],
                   1001,
                   request.form['latitude'],
                   request.form['longitude']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))		
