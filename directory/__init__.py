from sqlite3 import dbapi2 as sqlite3
from flask import Flask, g, request
from contextlib import closing

# __name__ is the name of the current module
app = Flask(__name__)

app.config.update(dict(
	DATABASE='/tmp/adventure.db', # why put it in tmp? because you don't want to version control it and this way the OS will clean it up for you
        PHOTOS = '/static/images/', # location of place images
        TILE_SERVER = 'localhost', # location of map tiles
        DEBUG=True,
))

# TODO : Look up config.from_envvar
# what is this for? "silent"?
#app.config.from_envvar('ADVENTURE_SETTINGS', silent=False)

def connect_db():
        "Connects to the database, returns a connection object"
	return sqlite3.connect(app.config['DATABASE'])

# This adds the schema and data to the database. 
# It also adds a user with the given password (hashed).
def init_db(password):
    with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		with app.open_resource('database.sql', mode='r') as f:
			db.cursor().executescript(f.read())
                with app.open_resource('counties.sql', mode='r') as f:
                        db.cursor().executescript(f.read())
		from directory import users
                admin_user = users.User("admin", password)
                db.execute(dbinserts.add_new_user, 
                           [admin_user.username, admin_user.pw_hash])
                db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
  db = getattr(g, 'db', None)
  if db is not None:
    db.close()

# This runs views
from directory import views

# this runs the app 
if __name__ == '__main__':
	app.run()
