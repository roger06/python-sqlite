import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("""SELECT * FROM students""")

# get all
print(c.fetchall())
# get all
print(c.fetchall())
# get all
print(c.fetchall())

conn.commit()
conn.close()
print ("query results")

