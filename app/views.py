from flask import Blueprint
from app.controllers import register_user, login_user, refresh_token, logout_user, create_todo, get_todos, update_todo, delete_todo

main_bp = Blueprint('main', __name__)

main_bp.route('/register', methods=['POST'])(register_user)
main_bp.route('/login', methods=['POST'])(login_user)
main_bp.route('/refresh', methods=['POST'])(refresh_token)
main_bp.route('/logout', methods=['POST'])(logout_user)
main_bp.route('/todos', methods=['POST'])(create_todo)
main_bp.route('/todos', methods=['GET'])(get_todos)
main_bp.route('/todos', methods=['PUT'])(update_todo)
main_bp.route('/todos', methods=['DELETE'])(delete_todo)

