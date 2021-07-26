import cgi
print("Content-Type: text/html")
print("")
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fieldss
print("<html>")
print("<body>")
U1=form.getvalue('Uname')
P1=form.getvalue('Pass')
password="admin"
username="admin"
if U1=username and P1= password:
    print("Name: {}".format(U1) "welcome to new page")
    
else:
    print('incorrect login credential')

print("</body>")
print ("</html>")
