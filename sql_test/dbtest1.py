import sqlite3

# 连接到SQLite数据库，建立数据库文件data.db,如果文件不存在，自动建立。
conn = sqlite3.connect('data.db')
# 创建一个cursor游标
cursor = conn.cursor()

# 执行一条SQL语句，创建user，包括账号user_id与密码password
cursor.execute('create table user (user_id varchar(30) primary key, password varchar)')

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭connection
conn.close()
