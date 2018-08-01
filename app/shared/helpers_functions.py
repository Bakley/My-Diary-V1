from app.models.usermodel import User

from flask import abort, jsonify, make_response

def sign_up_user(username, password, email):
    """A signup method to register a new user"""
    user = User.get_a_user(username)
    if user:
        response = {
            'error': 'Conflict',
            'message': 'User already exists. Choose a different username'
        }
        return make_response(jsonify(response)), 409

    user = User(username=username, email=email, password= password)
    user_id = user.create_user()

    response = {
        'message': 'Signed up successfully',
        'username': user.username,
        'id': user_id
    }
    return make_response(jsonify(response)), 201


def log_in_user(username, password):
    """A login method thats logs in an existing user"""
    user = User.get_a_user(username)

    if not user:
        response = {
            'message': 'User account does not exist'
        }
        return make_response(jsonify(response)), 401

    if user.verify_password(password):
        # JWT Authorization
        token = user.generate_auth_token()
        response = {
            'message': 'Logged in successfully',
            'access_token': token.decode('UTF-8')
        }
        return make_response(jsonify(response)), 200

    # If wrong password
    response = {
        'message': 'Invalid user credentials'
    }
    return make_response(jsonify(response)), 401