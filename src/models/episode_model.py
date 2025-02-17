from models import db, ma

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    air_date = db.Column(db.String(255))
    episode = db.Column(db.String(50))
    characters = db.relationship('Character', secondary="characters_episodes", back_populates='episodes', lazy=True)

class EpisodeOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()
    episode = ma.String()
