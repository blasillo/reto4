#!/usr/bin/python
print('Content-Type: text/plain')
print('')
print("Future exam questions and answers:")

import MySQLdb
db=MySQLdb.connect(host="192.168.4.20",user="root",db="sirs",password="password")
c=db.cursor()
c.execute("""SELECT id, question, answer, publish_date FROM exams WHERE publish_date > NOW()""")
rows = c.fetchall()

for row in rows:
  print(row)
