#!/home/shah/yes/bin/python

print("Content-Type: text/HTML")
print()
import cgi

#print("<center><h1>This is your sign up page</h1></center>")
print("<hr/>")


form = cgi.FieldStorage()
'''
user_name ='abcd' #
pwd = 123#
clg = 'qw'#
dept = 'ds'#
type = 222
'''
email = form.getvalue("email")
pwd=form.getvalue("pwd")
name = form.getvalue("name")
clg = form.getvalue("college_code")
gender = form.getvalue("gender")
mobile = form.getvalue("mobile")

#print(user_name,pwd,clg,dept,type)

import mysql.connector

con = mysql.connector.connect(user='root',password='',host='localhost',database='result_demo')
cur = con.cursor()

try:
    cur.execute("INSERT INTO user(EMAIL,PASSWORD,USERNAME,COLLEGE,GENDER,MOBILE) values(%s,%s,%s,%s,%s,%s)",tuple(list([email,pwd,name,clg,gender,mobile])))
    #print("<br><br><h1>Successful logged in</h1>")
    print("""
    <body>
    <script>
        alert("Record successfully entered for {}");
    </script>
    </body>
    """.format(email))
    redirectURL = "i.html"
    print('    <meta http-equiv="refresh" content="0;url=' + str(redirectURL) + '" />')
except:
    redirectURL = "member.py"
    print('<html>')
    print('  <head>')
    print("""
    <script>
  alert("PLease enter another username");
  </script>
  """)
    print('    <meta http-equiv="refresh" content="0;url=' + str(redirectURL) + '" />')
    print('  </head>')
    print('</html>')

#SELECT DECODE(PASSWORD, 'secret') AS `pswd` FROM `user` WHERE COLLEGE='OTHER';

"""
"""





#print("<html>Record successfully entered for </html>",name)

con.commit()
cur.close()
con.close()
#print("<hr/>")
#print("Connection closed")
#print("<a href='home.html'>Home</a>")