import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
    CREATE TABLE food(
    
      id TEXT PRIMARY KEY ,
      desc TEXT ,
      water FLOAT ,
      kcal FLOAT ,
      protein FLOAT ,
      fat FLOAT ,
      ash FLOAT ,
      carbs FLOAT ,
      fiber FLOAT ,
      sugar FLOAT 
    )
    ''')
query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
filed_count = 10
for line in open('ABBREV.text'):
    fileds = line.split('^')
    vals = [convert(f) for f in fileds[:filed_count]]
    curs.execute(query, vals)
conn.commit()
conn.close()