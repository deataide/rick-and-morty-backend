from src.models import db, ma

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255))
    dimension = db.Column(db.String(255))
    characters_origin = db.relationship('Character', foreign_keys='Character.origin_id', back_populates='origin', lazy=True)
    characters_location = db.relationship('Character', foreign_keys='Character.location_id', back_populates='location', lazy=True)
        
class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    
    residents_count = ma.Method('get_residents_count')
    dimension = ma.String()
    def get_residents_count(self, obj):
        return len(obj.characters_location)