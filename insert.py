import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("""INSERT INTO students VALUES ('Hadley', 'Holden', 156756657)""")


conn.commit()
conn.close()
print ("hello")

