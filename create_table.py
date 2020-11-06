import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("""CREATE TABLE students (
                firstname text,
                lastname text,
                studentid integer

        )""")


conn.commit()
conn.close()
print ("hello")

