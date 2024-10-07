from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'XXXXXXXXX@qq.com'
app.config['MAIL_PASSWORD'] = 'XXXXXXXXX'

mail = Mail(app)