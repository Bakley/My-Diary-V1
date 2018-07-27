from app import app
from app.models.usermodel import User
from app.shared.helpers_functions import sign_up_user, login_user
from app.shared.validators import Validate

from flask import request, jsonify, abort, make_response

@app.route('/mydiary/api/v1/user/<username>', methods=['GET'])
def user_details(username):
    """Gets information about a specific user"""
    access_token = request.headers.get("Authorization")
    if not access_token:
        abort(401, "Please provide an access token to verify user")

    # verify.token(access_token)
    user = User.get_a_user(username)

    if not user:
        response = {
            'error': 'Not found',
            'message': 'User cannot be found'
        }
        return make_response(jsonify(response)), 404

    response = {
        'username': user.username
    }
    return make_response(jsonify(response)), 200


# Handles Multiple error for differnet case
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
