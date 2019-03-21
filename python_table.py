#!/home/shah/yes/bin/python


print("Content-Type: text/html")
print()
import cgi

import mysql.connector


form = cgi.FieldStorage()
session = form.getvalue("session")
branch = form.getvalue("branch")
sem = form.getvalue("sem")
section = form.getvalue("section")
subject = form.getvalue("subject")



#print(section,sem,session,subject,branch)
print("<br>")

print("This python script is executed!!!!")


def htmlTop():
    print("""<!html lang='en'>
              <head>
                  <title>this is the demo of data display</title>
              </head>    
               <body>   

  """)

print("the student is of ",section)
def htmlBottom():
    print("""
      </body></html>
  """)

def connectDB():
    con = mysql.connector.connect(user='root', password='', host='localhost', database='result_demo')
    cur = con.cursor()
    return con, cur




def select(con, cur):
    sql = """
    select ROLL_NO,SUBJECT_CODE,EXTERNAL,SECTION from MASTER_TABLE where 
    (GRADE='F'
    AND SESSION= {}  AND BRANCH_CODE = {} and SEMESTER= {} AND SECTION={} AND SUBJECT_CODE = {}) """.format(session,branch,sem,section,subject)
    cur.execute(sql)
    myresult = cur.fetchall()
    total=len(myresult)
    return myresult,total






def print_data(result):
    print("<center>")
    print("""
    <table border= "1px">
    <tr>
    <th style ="font-color:'red'">ROll_NO</th>
    <th>SUBJECT_CODE</th>
    <th>EXTERNAL</th>
    <th>SECTION</th>
    </tr>
    """)
    for each in result:

        print("<tr>")
        print("<td align =\"center\">{}</td>".format(each[0]))
        print("<td align =\"center\">{}</td>".format(each[1]))
        print("<td align =\"center\">{}</td>".format(each[2]))
        print("<td align =\"center\">{}</td>".format(each[3]))
        print("</tr>")
    print("</center></table>")


if __name__ == "__main__":
    htmlTop()
    db, cursor = connectDB()
    result,total = select(db, cursor)
    print("<center>The total no. of records fetched are <mark><b>",total,"</b></mark></center>")
    print_data(result)
    htmlBottom()

# con.commit()
# cur.close()
# con.close()
print("<br>")

# print("the connection is closed")


print("""<button><a href='enter_url.html'>Another Result</a></button>""")
print("""<button><a href='sec.html'>Another Analysis</a></button>""")
