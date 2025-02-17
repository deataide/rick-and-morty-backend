from services.character_service import CharacterService
from flask import jsonify, request

class CharacterController: 
    
    def __init__(self):
        self.character_service = CharacterService()

    def get_character_by_id(self, character_id):
        try:
            data = self.character_service.get_character_by_id(character_id)
            if isinstance(data, tuple):
                return jsonify(data[0]), data[1]

            return jsonify(data), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500 

    def get_characters_by_name(self):
        try:
            params = request.args.to_dict()
            name_starts_with = params.get('nameStartsWith', 'rick')

            try:
                page = int(params.get('page', 1))
                if page < 1:
                    raise ValueError
            except ValueError:
                return jsonify({"message": "Page must be a positive integer"}), 400

            data = self.character_service.get_characters_by_name(name_starts_with, page)

            if isinstance(data, tuple):
                return jsonify(data[0]), data[1]

            return jsonify(data), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
