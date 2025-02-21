from repositories.character_repository import CharacterRepository
from models.character_model import character_output, characters_output
from werkzeug.exceptions import NotFound

class CharacterService:
    
    def __init__(self):
        self.character_repository = CharacterRepository()
    
    def get_character_by_id(self, character_id: int):
        character = self.character_repository.get_character_by_id(character_id)
        if not character:
            raise NotFound("Character not found")      
        
        serialized_character = character_output.dump(character)

        return serialized_character

    def get_characters_by_name(self, name_starts_with: str, page):

        offset = (page - 1) * 20
        characters_data = self.character_repository.get_characters_by_name(name_starts_with, offset)
        if not characters_data:
            raise NotFound("Characters not found") 
    
        serialized_characters = characters_output.dump(characters_data["characters"])

        return {
            "characters": serialized_characters,
            "total_pages": characters_data["total_pages"]
        }
