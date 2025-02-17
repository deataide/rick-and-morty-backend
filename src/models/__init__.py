from flask_sqlalchemy import SQLAlchemy
from marshmallow import validate, fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()

from models.character_episodes import Characters_Episodes
from models.location_model import Location
from models.episode_model import Episode
from models.character_model import Character
