from controllers.character_controller import CharacterController
from flask import Blueprint, request

character_controller = CharacterController()
characters_bp = Blueprint('characters_bp', __name__)

@characters_bp.route('/characters/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    print('oxi')
    return character_controller.get_character_by_id(character_id)

@characters_bp.route('/characters', methods=['GET'])
def get_characters_by_name():
    return character_controller.get_characters_by_name()