from models import ma, db
from marshmallow import validate, fields, post_dump

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50))
    species = db.Column(db.String(255))
    type = db.Column(db.String(255))
    gender = db.Column(db.String(50))
    image = db.Column(db.String(255))
    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    origin = db.relationship('Location', foreign_keys=[origin_id], back_populates='characters_origin', lazy=True)
    location = db.relationship('Location', foreign_keys=[location_id], back_populates='characters_location', lazy=True)
    episodes = db.relationship(
        'Episode', secondary="characters_episodes", back_populates='characters', lazy=True)       
    
class BaseCharacterOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    image = ma.String()
    gender = ma.String()
    origin = ma.Nested("LocationOutput")
    location = ma.Nested("LocationOutput")

class ManyCharactersOutput(BaseCharacterOutput):
    episodes = ma.Nested("EpisodeOutput", many=True)
    @post_dump
    def last_episode(self, data, many, **kwargs):
        if data.get("episodes"):
            data["last_episode"] = data["episodes"][-1]
            data.pop("episodes")
        return data

class SearchCharacterByIdInput(ma.Schema):
    id = ma.Integer(required=True)

class SearchCharacterByNameInput(ma.Schema):
    name = ma.String(required=True, validate=validate.Length(min=3, max=50))

search_character_by_name = SearchCharacterByNameInput()
search_character_by_id = SearchCharacterByIdInput()
character_output = BaseCharacterOutput()
characters_output = ManyCharactersOutput(many=True)
