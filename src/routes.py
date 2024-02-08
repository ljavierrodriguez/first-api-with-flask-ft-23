from flask import Blueprint, jsonify, request
from models import db, Note

api = Blueprint('api', __name__)

@api.route('/notes', methods=['GET'])
def get_notes():
    
    notes = Note.query.all() # [<Note 1>, <Note 2>]
    print(notes)
    notes = list(map(lambda note: note.serialize(), notes))
    print(notes) # [{"id": 1, "message": "Hello World!", "status": "active"}]
    return jsonify(notes), 200

@api.route('/notes', methods=['POST'])
def create_note():
    
    datos = request.get_json()
    print(datos['message'])
    print(datos['status'])
    
    message = request.json.get('message')
    status = request.json.get('status')
    print(message)
    print(status)
    
    note = Note()
    note.message = message
    note.status = status
    
    db.session.add(note) 
    db.session.commit()
    
    
    
    return jsonify(note.serialize()), 201

@api.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    
    datos = request.get_json()
    
    if not 'message' in datos: return jsonify({ "msg": "Field message is required!"}), 400
    
    note = Note.query.get(id) # None
    
    if not note: return jsonify({"msg": "Note doesn't exist!"}), 404
    
    note.message = datos['message']
    note.status = datos['status']
    
    db.session.commit() # guarda los cambios permanentemente
    
    return jsonify(note.serialize())

@api.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    
    note = Note.query.get(id) # None
    
    if not note: return jsonify({"msg": "Note doesn't exist!"}), 404
    
    db.session.delete(note)
    db.session.commit()
    
    return jsonify({"msg": "Note was deleted!"}), 200
