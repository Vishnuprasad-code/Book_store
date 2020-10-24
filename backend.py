import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text,year integer, ISBN integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,ISBN):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,ISBN))
    conn.commit()
    conn.close()   

def view():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM books")
    rows=curr.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM books WHERE title=? or author=? or year=? or ISBN=?",(title,author,year,isbn))
    rows=curr.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("UPDATE books SET title=?,author=?,year=?,ISBN=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


def delete(id):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()


