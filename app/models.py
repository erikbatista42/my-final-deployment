# Create your models here.
from sqlalchemy_utils import URLType
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    # The Gamestop - Who created it?
    gamestops = db.relationship('Gamestop', back_populates='user')
    

class Gamestop(db.Model):
    """Gamestop model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    games = db.relationship('Game', back_populates='gamestop')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='gamestops')

class Game(db.Model):
    """Game model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    photo_url = db.Column(URLType)
    
    gamestop_id = db.Column(db.Integer, db.ForeignKey('gamestop.id'), nullable=False)
    gamestop = db.relationship('Gamestop', back_populates='games')