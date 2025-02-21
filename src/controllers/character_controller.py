from services.character_service import CharacterService
from flask import jsonify, request
from utils.api_response import ApiResponse
from werkzeug.exceptions import NotFound

class CharacterController: 
    
    def __init__(self):
        self.character_service = CharacterService()

    def get_character_by_id(self, character_id):
        try:
            data = self.character_service.get_character_by_id(character_id)
            return ApiResponse.response(True, 'Character', data, 200)
        
        except NotFound as f:
            return ApiResponse.response(False, 'Character not found', None, 404)
        
        except Exception as f:
            return ApiResponse.response(False, f.args[0], None, 500)

    def get_characters_by_name(self, name_starts_with, page):
        try:
            data = self.character_service.get_characters_by_name(name_starts_with, page)
            return ApiResponse.response(True, 'Characters', data, 200)
        
        except NotFound as f:
            return ApiResponse.response(False, 'Characters not found', None, 404)

        except Exception as f:
            return ApiResponse.response(False, f[0], None, 500)
