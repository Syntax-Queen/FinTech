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