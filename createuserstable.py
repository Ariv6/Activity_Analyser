import sqlite3

conn = sqlite3.connect('database.db')
print('Opened databases successfully!')
conn.execute('CREATE TABLE activities (username TEXT, activity TEXT, minutes TEXT, day TEXT)')
print('Table created successfully!')
conn.close()