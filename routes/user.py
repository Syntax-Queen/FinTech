from app import app, db
from flask import  Flask, jsonify, request
from flask_cors import cross_origin 
from toolz import random_generator, validate_email
from models import User
from auth import auth
from datetime import datetime, timedelta
import uuid
import os
from dotenv import load_dotenv

load_dotenv() 
@app.route('/signup', methods=['POST'])
cross_origin
def signup():
    data = request.json
    username = data.get('username')
    phone = data.get('phone')
    email = data.get('email')
    nin = data.get('nin')
    password = data.get('password')

    if noot all([username, phone, email, password, nin]):
        return jsonify({'error' : 'All field (username, phone, email, password, nin) are required.'}), 400

    
    if  not username and len(username) < 3:
        return jsonify({'error' : 'Username must be at least 3 characters long.'}), 400


    if not phone and  not str(phone).isdigit():
        return jsonify({'error': 'Phone number must contain only digits'}), 400

    if not validate_email(email):
        return jsonify({'error': 'Enter a valid email address'}), 400

    if not str(nin).isdigit():
        return jsonify({'error': 'NIN must contain only digits.'}), 400

    
    if len(str(phone)) < 10:
        return jsonify({'error': 'Phone number must be at least 10 digits long.'}), 400

    
    if password is None and len(password) < 8:
        return jsonify({'error' : 'Password is invalid, please enter 8 or more characters'}), 400

    # check if phone or email already exists
    existing_user = User.query.filter(
        (User.phone == phone) | (User.email == email)
    ).first()

    if existing_user:
        return jsonify('error': 'User with this phone or email already exists.'), 400

    new_user = User(
        id = str(uuid.uuid4()),
        username = username,
        phone = phone,
        email = email,
        nin = nin,
    )
    db.session.add(new_user)
    new_user.set_password(password)

    try:
        db.session.commit()

        # send email successfully
        
    
