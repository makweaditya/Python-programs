import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='python_mindcoder'
)

cursor = connection.cursor()

sql = "INSERT INTO students (id, name, age, city) VALUES (10, 'raj', 13, 'indore')"

cursor.execute(sql)
connection.commit()
connection.close()

print('data inserted successfully')
