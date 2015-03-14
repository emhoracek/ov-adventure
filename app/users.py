from app import g
from werkzeug.security import generate_password_hash, check_password_hash

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        
    def add_to_database(self, password, db): 
        db.execute(dbinserts.add_new_user, 
                     [username, self.set_password(password)])

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
