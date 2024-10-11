import random
from my_app import app
from sendmail import send_register_mail, send_password_reset_email
from flask_mail import Message
from flask import render_template, session, request, url_for, redirect, abort, \
                    flash, get_flashed_messages, g

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
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        token = random.randint(1000, 9999)
        send_register_mail(email, username=username, token=token)
        session['token_register'] = str(token)
        session['email_save'] = email
        session['password_save'] = password
        session['username_save'] = username
        return redirect(url_for('register_email_page'))
    
@app.route('/register-email')
def register_email_page():
    return render_template('register-email.html')