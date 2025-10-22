from flask import make_response, jsonify
from models import User
from flask_httpauth import HTTPTokenAuth

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Authorized access'}), 401)

@auth.verify_token
def verify_token(token):
    return User.verify_auth_token(token)