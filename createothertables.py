import sqlite3
import time 
import datetime

conn = sqlite3.connect('database.db')
print('Opened databases successfully!')
username = 'Ariv'
activity = 'Study'
day = 'Thursday'
minutes = '60'
conn.execute("INSERT INTO activities (username, activity, minutes, day) VALUES (?, ?, ?, ?)", [username, activity, minutes, day])

print(f"username: {username}, activity: {activity}, day: {day}, minutes: {minutes}")

print('value inserted successfully!')
conn.close()


