#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection
form=cgi.FieldStorage()
uid=form.getvalue('name')
try:
    con=connection.connect()
    if con:
        cursor=con.cursor()
        cursor.execute("select distinct balance from balance where uid='%s'"%(uid))
        rows=cursor.fetchall()
        if not rows:
            print("no record")
        else:
            for i in rows:
                print("your balance is:Rs. ",i[0])
        #print("<h1>your balance is",b,"</h1>")
    else:
        print("<h1>connection not established...</h1>")
except:
    print("failed....")
finally:
    con.commit()
    con.close()
