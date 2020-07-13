import sqlite3

def create_table():
  # connect to db
  conn = sqlite3.connect("lite.db")
  # create a cursor object
  cur = conn.cursor()
  # execute sql statement
  cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, qty INTEGER,  price REAL)")

  conn.commit()
  conn.close()

def insert(item, qty, price):
  conn = sqlite3.connect("lite.db")
  # create a cursor object
  cur = conn.cursor()
  # execute sql statement
  cur.execute("INSERT INTO store values (?,?,?)", (item, qty, price))

  conn.commit()
  conn.close()

insert("Coffee Cup", 9, 10.8)

def view():
  conn = sqlite3.connect("lite.db")
  # create a cursor object
  cur = conn.cursor()
  # execute sql statement
  cur.execute("SELECT * FROM store")
  rows = cur.fetchall()

  conn.close()
  return rows

print(view())

def delete(item):
  conn = sqlite3.connect("lite.db")
  # create a cursor object
  cur = conn.cursor()
  # execute sql statement
  cur.execute("DELETE FROM store where item=?", (item,))

  conn.commit()
  conn.close()

delete("Coffee Cup")
print(view())
