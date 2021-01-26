"""
> pip install mysql-connector-python
"""

import mysql.connector

dbconfig = {
    'host': '127.0.0.1',
    'user':'root',
    'password': '856-Kim-856',
    'database': 'vsearchlogDB'
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = '''show tables''' #'''describe log'''
cursor.execute(_SQL)
res = cursor.fetchall()
print(res)

cursor.fetchall()

conn.commit()

cursor.close()
conn.close()
