"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Todo
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

@api.route('/todos', methods=['GET'])
def get_all_todos():
    todos = Todo.query.all()
    todos_serialized = [todo.serialize() for todo in todos]
    return jsonify({"todos": todos_serialized}), 200

@api.route('/todo', methods=['POST'])
def create_todo():
    body = request.json
    new_todo = Todo(done=body['done'], label=body['label'], user_id=body['user_id'])
    db.session.add(new_todo)
    db.session.commit()
    response_body = {"Todos": "Todo created successfully"}
    return jsonify(response_body), 200

@api.route('/todo/<int:todo_id>', methods=['GET'])
def get_one_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"erro": "Not able to find Todo with the provided id."}), 400
    return jsonify({'todo': todo.serialize()}), 200

@api.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Not todo found with this id"}), 400
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"todo": "Deleted"}), 200