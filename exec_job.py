from dbops.connection import db_connection

conn = db_connection()
cursor = conn.cursor()

cursor.execute('SELECT customer_id FROM dw.d_customer LIMIT 1;')
print(cursor.fetchone())