import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='python_mindcoder'
)

cursor = connection.cursor()

sql = "UPDATE students SET age = 15, city = 'Bhopal' WHERE id = 10"

cursor.execute(sql)
connection.commit()
connection.close()

print("Record updated successfully")
