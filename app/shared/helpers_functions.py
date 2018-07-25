from app.models.usermodel import User, diaryEntry
from flask import abort, jsonify, make_response

def sign_up_a_user(username, password, email):
    user = User.get_a_user(username)
    if user:
        response = {
            'error': 'Conflict',
            'message': 'User already exists'
        }
        return make_response(jsonify(response)), 409
    
    user = User(username=username)
    user.hash_password(password)
    user.email =email
    user_id = user.a

    response = {
        'message': 'Signed up successfully',
        'username': user.username,
        'id': user_id,
        'email': email
    }