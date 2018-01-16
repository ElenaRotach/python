import sqlite3 
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("CREATE TABLE currency_pair (id INTEGER, name text, description text)")
c.execute("INSERT INTO currency_pair VALUES ('1','EUR/USD','')")
conn.commit()
conn.close()