from datetime import datetime, timedelta
import os
import jwt
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nin = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    #  # verify phone number
    # is_phone_verified = db.Column(db.Boolean, default=False)
    # phone_otp = db.Column(db.String(6), nullable=True)
    # otp_expires_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def generate_auth_token(self):
        expiration_time = datetime.utcnow() + timedelta(days=10)
        payload = {
            'id' : self.id,
            'exp' : expiration_time
        }
        token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')
        return token


        @staticmethod
        def verify_auth_token(token):
            if not token:
                return None

            try:
                active_token = StoredjwtToken.query.filter_by(jwt_token=token).first()

                if active_token:
                    payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
                user = User.query.get(payload['id'])
                return user
            except jwt.ExpiredSignatureError:
                print("Token has expired")
                return None
            except jwt.DecodeError:
                print("Token is invalid")
                return None


       
class StoredjwtToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jwt_token = db.Column(db.String(255), unique=True, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    
    
class PasswordResetToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    used = db.Column(db.Boolean, nullable=False, default=False)
    generated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

   