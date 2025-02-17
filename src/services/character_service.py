from repositories.character_repository import CharacterRepository
from models.character_model import search_character_by_id, character_output, characters_output

class CharacterService:
    
    def __init__(self):
        self.character_repository = CharacterRepository()
    
    def get_character_by_id(self, character_id: int):

        character = self.character_repository.get_character_by_id(character_id)
    
        if not character:
            return {"message": "Character not found"}, 404
        
        serialized_character = character_output.dump(character)

        return serialized_character

    def get_characters_by_name(self, name_starts_with: str, page):
        try:
            page = int(page)
            if page < 1:
                raise ValueError
        except ValueError:
            return {"message": "Page must be a positive integer"}, 400

        offset = (page - 1) * 20
        
        characters_data = self.character_repository.get_characters_by_name(name_starts_with, offset)

        serialized_characters = characters_output.dump(characters_data["characters"])

        return {
            "characters": serialized_characters,
            "total_pages": characters_data["total_pages"]
        }
