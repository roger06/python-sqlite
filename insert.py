import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("""INSERT INTO students VALUES ('Roger', 'Holden', 7265)""")


conn.commit()
conn.close()
print ("hello")

