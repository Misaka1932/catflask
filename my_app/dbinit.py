import sqlite3
from werkzeug.security import check_password_hash, \
                            generate_password_hash

def createdb():
    # 连接到SQLite数据库, 建立数据库文件data.db, 如果文件不存在自动建立。
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # 创建user 包括
    # id
    # 用户名username
    # 密码哈希值password
    # 用户邮箱
    try:
        cursor.execute('''create table user (
                        id integer primary key AUTOINCREMENT,
                        username varchar(30),
                        password_hash varchar(500),
                        email varchar(50)
                    )''')
        conn.commit()
    except:
        print('Already have database')

    cursor.close()
    conn.close()

def get_password_hash(password):
    return generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)

def add_user(username, password, email):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    password_hash = get_password_hash(password)

    # print(password_hash)
    # print(password)
    # print(email)
    # print(username)
    cursor.execute('insert into user(username,password_hash,email) values(?,?,?)', 
                    (username, password_hash, email))
    conn.commit()
    cursor.close()

def check_password(email, password):

    # 以后可能会修改返回值 这样感觉可以更清楚知道哪里错了
    # 暂时就用True和False了
    
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(f'select * from user where email="{email}"')
    
    rowcount = cursor.rowcount
    result = cursor.fetchone()
    # print('result: ', result)
    # print('rowcount: ', rowcount)

    if result:
        result = result[2]
    else:
        return False
    
    cursor.close()
    if check_password_hash(result, password):
        return True
    else:
        return False
    


# createdb()
# add_user('Admin', '123456', 'mitruha@qq.com')
# print(check_password('Admin', '123456'))