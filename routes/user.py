from app import app, db
from flask import Flask, jsonify, request
from flask_cors import cross_origin 
from toolz import random_generator, validate_email
from models import User
# from auth import auth
from datetime import datetime, timedelta
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

@app.route('/signup', methods=['POST'])
# @cross_origin/
def signup():
    data = request.json
    username = data.get('username')
    phone = data.get('phone')
    email = data.get('email')
    nin = data.get('nin')
    password = data.get('password')

    if not all([username, phone, email, password, nin]):
        return jsonify({'error': 'All field (username, phone, email, password, nin) are required.'}), 400

    if not username and len(username) < 3:
        return jsonify({'error': 'Username must be at least 3 characters long.'}), 400

    if not phone and not str(phone).isdigit():
        return jsonify({'error': 'Phone number must contain only digits'}), 400

    if not validate_email(email):
        return jsonify({'error': 'Enter a valid email address'}), 400

    if not str(nin).isdigit():
        return jsonify({'error': 'NIN must contain only digits.'}), 400

    if len(str(phone)) < 10:
        return jsonify({'error': 'Phone number must be at least 10 digits long.'}), 400

    if password is None and len(password) < 8:
        return jsonify({'error': 'Password is invalid, please enter 8 or more characters'}), 400

    # check if phone or email already exists
    existing_user = User.query.filter(
        (User.phone == phone) | (User.email == email)
    ).first()

    if existing_user:
        return jsonify({'error': 'User with this phone or email already exists.'}), 400

    new_user = User(
        id=str(uuid.uuid4()),
        username=username,
        phone=phone,
        email=email,
        nin=nin,
    )
    new_user.set_password(password)
    db.session.add(new_user)

    try:
        db.session.commit()

        # send welcome email
        subject = "Welcome to Fin Tech  Your Identity-Protected Payment Platform 🔒"

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Welcome to Fin Tech</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f8f9fa;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: 40px auto;
                    background-color: #ffffff;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background-color: #0d6efd;
                    color: #ffffff;
                    text-align: center;
                    padding: 30px 20px;
                }}
                .header h2 {{
                    margin: 0;
                }}
                .content {{
                    padding: 30px 20px;
                    line-height: 1.6;
                }}
                .cta {{
                    display: inline-block;
                    background-color: #0d6efd;
                    color: #fff;
                    text-decoration: none;
                    padding: 12px 20px;
                    border-radius: 6px;
                    margin-top: 20px;
                }}
                .footer {{
                    font-size: 13px;
                    color: #777;
                    text-align: center;
                    padding: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h2>Welcome to Fin Tech, {username}! 🔒</h2>
                </div>
                <div class="content">
                    <p>We’re thrilled to have you join <strong>Fin Tech</strong>  the privacy-first payments platform that protects your real identity when sending or receiving money.</p>

                    <h3>Here’s what you can do with Fin Tech:</h3>
                    <ul>
                        <li>Send and receive money securely using only your <strong>username</strong>  your real name stays hidden.</li>
                        <li>Buy airtime, data, and pay electricity bills  all within the app.</li>
                        <li>Sign in safely using <strong>face or fingerprint scanning</strong> for stronger protection.</li>
                        <li>Verify your account with <strong>phone number, NIN, BVN, and email</strong> for trusted transactions.</li>
                    </ul>

                    <p>We designed Fin Tech to give you <strong>privacy, security, and full control</strong> over how your identity is shared during financial transactions. Your personal details remain encrypted and are only used when legally required.</p>

                    <p><a href="https://finhide.app/login" class="cta">Get Started</a></p>

                    <p>If you ever forget your credentials or need to verify a transaction, we’ll send secure verification tokens directly to your registered email.</p>

                    <p>Welcome to a new era of private, digital payments 🚀</p>
                </div>
                <div class="footer">
                    <p>Fin Tech  Privacy. Security. Freedom.</p>
                    <p>&copy; 2025 Fin Tech. All rights reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """

        email_sent = send_email(subject, email, text_body, html_body)

        if email_sent:
            return jsonify({'success': True, 'message': 'Account created and welcome email sent successfully.'}), 201
        else:
            return jsonify({'success': True, 'message': 'Account created, but failed to send email'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'User signup error: {e}'}), 500
