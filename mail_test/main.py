from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
import webbrowser
app = Flask(__name__)

app.config['MAIL_SERVER']   = 'smtp.qq.com'
app.config['MAIL_PORT']     = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS']  = False
app.config['MAIL_USE_SSL']  = True
mail = Mail(app)


@app.route('/write')
def write_mail():
    return render_template('write.html')

@app.route('/send' ,methods=['GET','POST'])
def send_mail():
    username=request.form.get('username')
    theme=request.form.get('theme')
    content=request.form.get('content')
    msg = Message(theme, sender=os.environ.get('MAIL_USERNAME'), recipients=[username],body=content)
    mail.send(msg)
    return '邮件发送成功'

if __name__ == '__main__':
    webbrowser.open_new('http://localhost:5000/write')
    app.run(debug = True)