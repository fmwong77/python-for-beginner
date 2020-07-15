import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER) ")
        self.conn.commit()
        # self.conn.close()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author=""):
        self.cur.execute("SELECT * FROM book WHERE title = ? or author = ?", (title, author))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book where id = ?", (id,))
        self.conn.commit()

    def update(self, id, title):
        self.cur.execute("UPDATE book set title = ? WHERE id = ?", (title, id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
