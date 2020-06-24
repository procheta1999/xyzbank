#!C:\Python34\pythonw.exe
import cgi
print("Content-type:text/html\r\n\r\n")
form=cgi.FieldStorage()
deposit=form.getvalue('m')
print("<h1>Rs. ",deposit," has been successfully deposited to your account.</h1>")
print("<a href='homepage.html'>back to homepage</a>")
