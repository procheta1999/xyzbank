#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

form=cgi.FieldStorage()
id=form.getvalue("t1")
pwd=form.getvalue("t2")
print(id)
try:
    conn=connection.connect()
    if conn:
        cursor=conn.cursor()
        cursor.execute("select * from login where userid='%s'"%(id))
        rows=cursor.fetchall()
        if not rows:
            print("no record found<a href='newacc.html'>new account</a>")
        else:
            print("login successful <a href='homepage.html'>homepage</a>")
    else:
        print("<h1>connection not established...</h1>")
except:
    print("failed to show data")
finally:
    conn.commit()
    conn.close()
