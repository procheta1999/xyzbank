#!C:\Python34\pythonw.exe
import mysql.connector
print ("Content-type:text/html\r\n\r\n")


def connect():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='bank_details',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print ("<h2>Connected Successfully</h2>")
            return conn 
    except:
        print ("<h2>Unable to connect serveR...</h2>")

connect()





 
  
