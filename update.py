#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection
form=cgi.FieldStorage()
ui=form.getvalue("t3")
p=form.getvalue("t4")
try:
    con=connection.connect()
    if con:
        cursor=con.cursor()
        sql="insert into login(userid,password) values (%s,%s)"
        cursor.execute(sql,(ui,p))
        print("<h1>successfully inserted</h1><a href='index.html'>back to login page</a>")
    else:
         print("connection not established")
except:
    print("<h1>user creation failed....</h1>")
finally:
    con.commit()
    con.close()
        
