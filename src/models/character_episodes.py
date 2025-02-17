from models import db

class Characters_Episodes(db.Model):
    __tablename__ = 'characters_episodes'
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
