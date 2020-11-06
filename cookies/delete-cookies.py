import sqlite3

# conn = sqlite3.connect("cookies.sqlite")
conn = sqlite3.connect("/home/roger/.mozilla/firefox/d2p7v063.default-release/cookies.sqlite")


c = conn.cursor()
 
 

sql  = """DELETE FROM moz_cookies where 
            host not like '%youtube%'  AND  
            host not like '%amazon%' AND 
            host not like '%barclays%' AND 
            host  not like '%facebook%'  AND 
            host not  like '%bbc%'  AND 
            host not  like '%bbc%' AND 
            host not  like '%mail.google.com%' AND 
            host not  like '%photos.google.com%' AND 
            host not  like '%photos.google.com%' AND 
            host not  like '%contacts.google.com%' AND 
            host not  like '%accounts.google.com%' AND 
            host not  like '%myaccount.google.com%' AND 
            host not like '%mendeley%' """


c.execute(sql)

conn.commit()

conn.close()
# print ("query results")

