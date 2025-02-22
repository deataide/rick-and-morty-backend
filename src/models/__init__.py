from flask_sqlalchemy import SQLAlchemy
from marshmallow import validate, fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()

from .character_episodes import Characters_Episodes
from .location_model import Location
from .episode_model import Episode
from .character_model import Character
