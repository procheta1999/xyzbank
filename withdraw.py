#!C:\Python34\pythonw.exe
import cgi
print("Content-type:text/html\r\n\r\n")
form=cgi.FieldStorage()
amount=form.getvalue('t')
print("<h1>Hello Rs.",amount," has been successfully withdrawn</h1>")
print("<a href='homepage.html'>back to homepage</a>")
