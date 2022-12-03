import psycopg2


class Database:
    def __init__(self):
        con = psycopg2.connect("dbname='database2',user='postgres',password='1234',host='localhost',port='5432'")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year INTEGER,rating INTEGER)")
        con.commit()
        con.close()

    def insert(self,title, author, year, rating):
        con = psycopg2.connect("dbname='database2',user='postgres',password='1234',host='localhost',port='5432'")
        cur = con.cursor()
        cur.execute("INSERT INTO book VALUES(NULL,%s,%s,%s,%s)", (title, author, year, rating))
        con.commit()
        con.close()

    def view(self):
        con = psycopg2.connect("dbname='database2',user='postgres',password='1234',host='localhost',port='5432'")
        cur = con.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        con.close()
        return rows

    def search(self, title="", author="", year="", rating=""):
        con = psycopg2.connect("dbname='database2',user='postgres',password='1234',host='localhost',port='5432'")
        cur = con.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR rating=?", (title, author, year, rating))
        rows = cur.fetchall()
        con.close()
        return rows

    def delete(self,iq):
        con = psycopg2.connect("dbname='database2',user='postgres',password='1234',host='localhost',port='5432'")
        cur = con.cursor()
        cur.execute("DELETE FROM book WHERE id=%s",(id,))
        con.commit()
        con.close()

    def update(self):
        con = psycopg2.connect("dbname='database2',user='postgres',password='1234',host='localhost',port='5432'")
        cur = con.cursor()
        cur.execute("UPDATE book SET title=%s,author=%s,year=%s,rating=%s WHERE id=%s ",(title,author,year,rating,id))
        con.commit()
        con.close()


