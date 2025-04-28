from flask import request, jsonify
from app import db
from app.models import User, Todo
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, unset_jwt_cookies

def register_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity=str(user.id))
        refresh_token = create_refresh_token(identity=str(user.id))
        return jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
@jwt_required()
def refresh_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({'access_token': access_token}), 200

@jwt_required()
def logout_user():
    unset_jwt_cookies(jsonify({'message': 'User logged out successfully'}))
    return jsonify({'message': 'User logged out successfully'}), 200

@jwt_required()
def create_todo():
    data = request.get_json()
    user_id = int(get_jwt_identity())
    new_todo = Todo(title=data['title'], description=data['description'], user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'}), 201

@jwt_required()
def get_todos():
    user_id = get_jwt_identity()
    todos = Todo.query.filter_by(user_id=user_id).all()
    return jsonify([{"title": todo.title, "description":todo.description, "user_id":todo.user_id} for todo in todos]), 200

@jwt_required()
def update_todo():
    data = request.get_json()
    todo = Todo.query.get(data['id'])
    if todo:
        todo.title = data['title']
        todo.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Todo updated successfully'}), 200
    return jsonify({'message': 'Todo not found'}), 404

@jwt_required()
def delete_todo():
    data = request.get_json()
    todo = Todo.query.get(data['id'])
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({'message': 'Todo deleted successfully'}), 200
    return jsonify({'message': 'Todo not found'}), 404