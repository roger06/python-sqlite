import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("""DELETE FROM students WHERE firstname = 'Hadley'""")


conn.commit()
conn.close()
print ("hello")

