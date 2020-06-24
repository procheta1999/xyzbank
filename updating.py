#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection
form=cgi.FieldStorage()
po=form.getvalue("t")
pn=form.getvalue("n")
try:
    con=connection.connect()
    if con:
        cursor=con.cursor()
        cursor.execute("update password set password='%s'"%(pn),"where password='%s'"%(po))
    
        print("<h1>successfully updated</h1><a href='homepage.html'>back to homepage</a>")
    else:
         print("connection not established")
except:
    print("<h1>updation failed....</h1>")
finally:
    con.commit()
    con.close()
        
