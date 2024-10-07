from flask import Flask
from flask_mail import Mail
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

'''
千万不要把账户密码直接写入代码中。
为了保护账户信息, 你需要让脚本从环境中导入敏感信息。

Windows 可以用setx设置环境变量 (记得重启电脑 不然get函数还是会识别成None)
setx MAIL_USERNAME = "homo@qq.com"     #发件人的用户名
setx MAIL_PASSWORD = "114514"          #发件人的POP3/IMAP/SMTP服务的SSL连接客户端授权码
'''

mail = Mail(app)