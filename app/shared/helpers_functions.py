from app.models.usermodel import User

from flask import abort, jsonify, make_response

def sign_up_user(username, password_hash, email):
    """A signup method to register a new user"""
    user = User.get_a_user(username)
    if user:
        response = {
            'error': 'Conflict',
            'message': 'User already exists. Choose a different username'
        }
        return make_response(jsonify(response)), 409

    user = User(username=username, password=password_hash, email=email)
    user.hash_password(password_hash)
    print("The hashed password == ", user.hash_password(password_hash)
)
    user.email = email
    user = user.create_user()

    response = {
        'message': 'Signed up successfully',
        # 'user': user
    }
    return make_response(jsonify(response)), 201


def log_in_user(username, password):
    """A login method thats logs in an existing user"""
    user = User.get_a_user(username)
    user_object = User(username, None, password)
    print("My user in log_in_user", user)

    if not user:
        print("My user after not if", user)
        response = {
            'message': 'User account does not exist'
        }
        return make_response(jsonify(response)), 401

    if user_object.verify_password(password, user[3]):
        # JWT Authorization
        token = user_object.generate_auth_token()
        print("The JWT =", token)
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