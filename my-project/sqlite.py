import sqlite3
conn = sqlite3.connect('..\lesson_sql\product_info.db')

cursor = conn.cursor()
cursor.execute('SELECT * FROM product_info')

sqlins = """
SELECT id, name FROM product_info 
WHERE id = "1"
"""

cursor.execute(sqlins)
records = cursor.fetchall()
print(records)

