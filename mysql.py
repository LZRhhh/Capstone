import MySQLdb
from pyface import search

filepath = "D:\Pictures\微信图片_20200224164925.jpg"
# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "admin", "bms", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

face_token = search(filepath)
# SQL 查询语句
sql = "SELECT id, username FROM user where face_token = \"%s\"" % face_token

# 使用execute方法执行SQL语句
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        print(id)
        username = row[1]
        print("Welcome, %s! " % username)
    sql = "select rack_id from user_rack where user_id = %s" % id
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        racks = []
        for row in results:
            racks.append(row[0])

    except:
        print("Error: unable to fetch %s's rack" % username)

except:
    print("Error: unable to fetch user")
print("You have access to ", racks)
# 关闭数据库连接
db.close()
