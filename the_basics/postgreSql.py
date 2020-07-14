import psycopg2

def create_table():
  # connect to db
  conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql123' host='localhost' port='5432'")
  # create a cursor object
  cur = conn.cursor()
  # execute sql statement
  cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, qty INTEGER,  price REAL)")

  conn.commit()
  conn.close()

def insert(item, qty, price):
  conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql123' host='localhost' port='5432'")
  # create a cursor object
  cur = conn.cursor()
  # execute sql statement
  cur.execute("INSERT INTO store values (%s, %s, %s)", (item, qty, price))

  conn.commit()
  conn.close()

# insert("Coffee Cup", 9, 10.8)

def view():
  conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql123' host='localhost' port='5432'")
  # create a cursor object
  cur = conn.cursor()
  # execute sql statement
  cur.execute("SELECT * FROM store")
  rows = cur.fetchall()

  conn.close()
  return rows

# print(view())

def delete(item):
  conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql123' host='localhost' port='5432'")
  # create a cursor object
  cur = conn.cursor()
  # execute sql statement
  cur.execute("DELETE FROM store where item=%s", (item,))

  conn.commit()
  conn.close()

def update(item, qty, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET qty=%s, price=%s WHERE item=%s",(qty, price, item))
    conn.commit()
    conn.close()



# create_table()
insert('Coffee Cup', 10, 100.5)
print(view())
# delete('Coffee Cup')
update('Coffee Cup', 5, 5.5)

