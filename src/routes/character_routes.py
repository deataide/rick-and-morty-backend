from controllers.character_controller import CharacterController
from flask import Blueprint, request
from flask import jsonify, request

character_controller = CharacterController()
characters_bp = Blueprint('characters_bp', __name__)

@characters_bp.route('/characters/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    return character_controller.get_character_by_id(character_id)

@characters_bp.route('/characters', methods=['GET'])
def get_characters_by_name():
    params = request.args.to_dict()
    name_starts_with = params.get('nameStartsWith', 'rick')
    page = int(params.get('page', 1)) if str(params.get('page', 1)).isdigit() else 1
    return character_controller.get_characters_by_name(name_starts_with, page)