from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(45), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(45), nullable = False)
    apitoken = db.Column(db.String)

    def __init__(self, username, email, password, apitoken):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.apitoken = apitoken

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

# Must have this function to send data to React
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'apitoken': self.apitoken
        }