#!/home/libby/.virtualenvs/outdoorRec/bin/python
from app import app, init_db

init_db()

app.run(debug=True)
