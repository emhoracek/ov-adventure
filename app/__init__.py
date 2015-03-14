from sqlite3 import dbapi2 as sqlite3
from flask import Flask, g, request
from contextlib import closing
from app import users


app = Flask(__name__)

app.config.update(dict(
	DATABASE='/tmp/adventure.db',
        DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
app.config.from_envvar('ADVENTURE_SETTINGS', silent=True)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db(password):
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		with app.open_resource('database.sql', mode='r') as f:
			db.cursor().executescript(f.read())
                with app.open_resource('counties.sql', mode='r') as f:
                        db.cursor().executescript(f.read())
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

from app import views

if __name__ == '__main__':
	app.run()
