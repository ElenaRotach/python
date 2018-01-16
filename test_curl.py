#import urllib.request
#import urllib.parse

url = 'https://www.deltastock.com/russia/instruments/forex-list.asp'
#f = urllib.request.urlopen(url)
#print(f.read().decode('utf-8'))

import requests
from pprint import pprint
# pip3 install pyquery
from pyquery import PyQuery as pq

import sqlite3 
id_paid = 0
r = requests.get(url)
#pprint(r.text)

d = pq(r.text)
t = d('table.comodities').children()
for tr in t:
	#pprint(pq(tr))
	tr = pq(tr)
	
	variable = str(id_paid)
	naim_paid = tr.children()[0].text
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	c.execute("INSERT INTO currency_pair VALUES ("+ variable +",'"+ naim_paid +"','')")
		#id_paid = c.fetchall()
	conn.commit()
	id_paid += 1
	conn.close()
	#pprint(tr.children()[0].text)
	"""for td in tr.children('td:first'):
		pprint(td.text)
		conn = sqlite3.connect('example.db')
		c = conn.cursor()
		c.execute("select count(id) from currency_pair")
		id_paid = c.fetchall()
		conn.commit()
		#pprint(id_paid[0][0])

		#naim_paid = pq(td)
#pprint(t)
"""