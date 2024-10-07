import random
from my_app import app
from sendmail import send_register_mail, send_password_reset_email
from flask import render_template, session, request, url_for, redirect
from flask_mail import Message

@app.route('/')
def empty_page():
    return redirect(url_for('home_page'))

@app.route('/home')
def home_page():
    return render_template('home.html')

'''
@app.route('/login')
def login_page():
    return render_template('login.html')
'''