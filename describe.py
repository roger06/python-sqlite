import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("""DESCRIBE students""")

# get all
# print(c.fetchall())

result = c.fetchall()

print(result)

#number_of_rows = cursor.execute(sql)

#result = c.fetchall()
#for row in result:
#  print(row[0], row[1])

 

#conn.commit()
#conn.close()
#print ("query results")

