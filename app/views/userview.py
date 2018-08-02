from app import app
from app.models.usermodel import User
from app.shared.helpers_functions import sign_up_user, log_in_user
from app.shared.validators import Validate

from flask import request, jsonify, abort, make_response



@app.route('/api/v1/auth/signup', methods=['POST'])
def signup_user():
    
    """Register a new user """
    if not request.is_json:
        abort(400, "Make sure you give data in json formart")
    # get the data in json format
    signup_request = request.get_json()
    if 'username' not in signup_request or 'password' not in signup_request:
        abort(400, 'Please make sure your username or password is in json format')
    
    username = signup_request['username']
    password = signup_request['password']
    email = signup_request['email']

    if username is None or password is None or email is None:
        abort(400, 'You have missing arguments')
    
    #Validate the Arguments given
    username_validation = Validate.validate_username(username)
    if not username_validation[0]:
        abort(401, username_validation[1])

    password_validation = Validate.validate_password(password)
    if not password_validation[0]:
        abort(401, password_validation[1])

    email_validation = Validate.validate_email(email)
    if not email_validation[0]:
        abort(401, email_validation[1])

    return sign_up_user(username, password, email)


@app.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    """Logs in an existing user"""
    if not request.is_json:
        abort(400, 'Make sure your data is in Json format')
    # Get the data in json format
    login_request = request.get_json()

    username = login_request['username']
    password = login_request['password']

    if username is None or password is None:
        abort(400, 'You have missing arguments')
    elif not username or not password:
        response = {
            'message': 'Please provide with username and password'
        }
        return make_response(jsonify(response)), 401

    #Validate the Arguments given
    username_validation = Validate.validate_username(username)
    if not username_validation[0]:
        abort(401, username_validation[1])

    password_validation = Validate.validate_password(password)
    if not password_validation[0]:
        abort(401, password_validation[1])
        
 
    return log_in_user(username, password)


@app.route('/api/v1/user/<username>', methods=['GET'])
def user_details(username):
    """Gets information about a specific user using the username    """
    access_token = request.headers.get("Authorization")
    if not access_token:
        abort(401, "Please provide an access token in order to verify user")

    verify_token(access_token)
    user = User.get_a_user(username)

    if not user:
        response = {
            'error': 'Not found',
            'message': 'User cannot be found in our Database'
        }
        return make_response(jsonify(response)), 404

    response = {
        'username': user.username
    }
    return make_response(jsonify(response)), 200

# @app.route('/api/v1/entry/entry_id', methods=['GET'])
# def get_an_entry(entry_id):
#     """Gets the only one entry"""
#     try:
#         entry_id = int(entry_id)
#     except ValueError:
#         entry_id = entry_id
    
#     if type(entry_id) is not int:
#         abort(400, "Please provide an interget in order to retrive the diary entry")
#     access_token = request.header.get("Authorization")

#     if not access_token:
#         abort(401, "Please provide an access token in order to verify user")

#     verify_token(access_token)
#     entry = Entries.get_an_entry(int(entry_id))

#     if not entry:
#         response = {
#             'error': 'Not found',
#             'message': 'Entry cannot be found in our Database'
#         }
#         return make_response(jsonify(response)), 404

# @app.route('/api/v1/users/entry', methods=['POST'])
# def create_entry():
#     """Endpoint for creating a new entry offer"""
#     if not request.is_json:
#         abort(400, 'Make sure your request contains json data')

#     access_token = request.headers.get('Authorization')
#     if access_token:
#         username = verify_token(access_token)

#         if not request.is_json:
#             abort(400, 'Make sure your request contains json data')

#         data = request.get_json()
#         if 'origin' not in data or \
#                 'destination' not in data:
#             abort(400,
#                   'Make sure you have specified name, '
#                   'origin and destination attributes in your json request.')

#         entry_offer = Entries(data['title'], data['description'])

#         print(username)
#         user = User.get_a_user(username)
#         entry_id = entry_offer.add_new_entry_offer(user.user_id)
#         response = {
#             'message': 'Ride created successfully',
#             'entry_id': entry_id,
#             'entry': convert_ride_offer(entry_id)
#         }

#         return make_response(jsonify(response)), 201
#     else:
#         abort(401, 'Please provide an access token')

def verify_token(access_token):
     """Verifies if the access token is correct"""
     username = User.decode_token(access_token)
     
     if username == "Invalid token. Please register or login":
         abort(401, username)
     elif username == "Token is expired. Please login again":
         abort(401, username)
     return username


# Handles Multiple error for differnet case
@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({"error": 'Internal Server Error',
                                  "message": error.description}), 500)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": 'Resource Not Found',
                                  "message": error.description}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": 'Bad request.',
                                  'message': error.description}), 400)


@app.errorhandler(409)
def conflict(error):
    return make_response(jsonify({"error": 'Conflict.',
                                  'message': error.description}), 409)


@app.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({"error": 'Unauthorized access.',
                                  'message': error.description}), 401)


@app.errorhandler(405)
def method_not_allowed(error):
    message = "{} Check the documentation for allowed methods".\
        format(error.description)
    return make_response(jsonify({"error": 'Method not allowed',
                                  "message": message}), 405)
