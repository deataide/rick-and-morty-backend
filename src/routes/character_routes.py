from src.controllers.character_controller import CharacterController
from flask import Blueprint, request
from flask import request
from . import cache

character_controller = CharacterController()
characters_bp = Blueprint('characters_bp', __name__)

@characters_bp.route('/characters/<int:character_id>', methods=['GET'])
@cache.cached(timeout=120, key_prefix=lambda: f"character_{request.view_args['character_id']}") 
def get_character_by_id(character_id):
    return character_controller.get_character_by_id(character_id)

@characters_bp.route('/characters', methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def get_characters_by_name():
    params = request.args.to_dict()
    name_starts_with = params.get('nameStartsWith', 'rick')
    page = int(request.args.get('page', 1))
    return character_controller.get_characters_by_name(name_starts_with, page)