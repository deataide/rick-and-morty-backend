from src.models.character_model import db, Character
import math

class CharacterRepository:
    
    def get_character_by_id(self, character_id: int):
        return db.session.get(Character, character_id)

    def get_characters_by_name(self, name_starts_with: str, offset: int = 0):

        try:
            query = Character.query.filter(Character.name.ilike(f"%{name_starts_with}%"))
            total_characters = query.count()
            characters = query.offset(offset).limit(20).all()
            total_pages = math.ceil(total_characters / 20)

            return {
                "characters": characters,
                "total_pages": total_pages
                }
            
        except Exception:
            db.session.rollback()
            raise
