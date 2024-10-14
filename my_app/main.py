import random
import logging
from my_app import app
from sendmail import send_register_mail, send_password_reset_email
from flask_mail import Message
from flask import Flask, render_template, session, request, url_for, redirect, abort, \
                    flash, get_flashed_messages, g, jsonify

'''
    g 作为 flask 程序全局的一个临时变量 充当中间媒介的作用 我们可以通过它传递一些数据
    注意: get_flashed_messages 这个模块需要在my_app里面设置secret_key
    在html模板中, 使用get_flashed_message()来获取消息。
'''

@app.route('/')
def empty_page():
    return redirect(url_for('home_page'))

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/404')
def not_found_page():
    return render_template('404.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == "GET":
        return render_template('register.html')
    
    else:
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        token = random.randint(100000, 999999)
        send_register_mail(email, username=username, token=token)
        session['token_register'] = str(token)
        session['email_save'] = email
        session['password_save'] = password
        session['username_save'] = username

        # app.logger.debug('register 具体信息')
        # app.logger.debug(email)
        # app.logger.debug(password)
        # app.logger.debug(username)
        # app.logger.debug('----------------')

        return redirect(url_for('register_email_page'))
    
@app.route('/agreement')
def agreement_page():
    return render_template('agreement.html')

@app.route('/register-email', methods=['GET', 'POST'])
def register_email_page():
    if request.method == "GET":
        return render_template('register.html')
    else:
        user_token = request.form.get('user_token')
        correct_token = session.get('token_register')

        # app.logger.debug('验证码具体信息')
        # app.logger.debug(user_token)
        # app.logger.debug(correct_token)
        # app.logger.debug('----------------')
        if user_token == correct_token:
            return redirect(url_for('blog_page'))
        else:
            error = '验证码错误!'
            # return jsonify({'status': '-1', 'text': '验证码错误!'})
            return render_template('register-email.html', error=error)
    
@app.route('/blog')
def blog_page():
    return render_template('blogpage.html')