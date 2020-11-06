import sqlite3

conn = sqlite3.connect("cookies.sqlite")

c = conn.cursor()
 
 
sql  = """SELECT host, name, value FROM moz_cookies where host  like '%youtube%'  or  host like '%amazon%' or host like '%barclays%' or host  like '%facebook%'  or host  like '%bbc%'  or host  like '%bbc%' 
 or host like '%mendeley%' order by name """
 
sql  = """SELECT host, name, value FROM moz_cookies  order by name """

 
 



c.execute(sql)
result = c.fetchall() 
# number_of_rows = c.execute(sql)

# print(result)
for row in result:
  print(row[0], row[1], row[2])

conn.close()
# print ("query results")

