#!/home/shah/yes/bin/python

print("Content-Type: text/HTML")
print()

import mysql.connector
import cgi

print("<br>")

print("This python script is executed!!!!")


def htmlTop():
  print("""<!html lang='en'>
              <head>
                  <title>this is the demo of data display</title>
              </head>    
               <body>   
  
  """)

def htmlBottom():
  print("""
      </body></html>
  """)


def connectDB():
  con = mysql.connector.connect(user='root', password='', host='localhost', database='result_demo')
  cur = con.cursor()
  return con,cur


def select(con,cur):
  sql = "select ROLL_NO,SUBJECT_CODE from MASTER_TABLE"
  cur.execute(sql)
  myresult = cur.fetchall()
  return myresult


def print_data(result):
  print("""
  <table border= "1px">
    <tr>
    <th style ="font-color:'red'">ROll_NO</th>
    <th>SUBJECT_CODE</th>
    </tr>
  """)
  for each in result:
    print("<tr>")
    print("<td>{}</td>".format(each[0]))
    print("<td>{}</td>".format(each[1]))
    print("</tr>")
  print("</table>")


if __name__== "__main__":
  htmlTop()
  db,cursor = connectDB()
  result = select(db,cursor)
  #print(result)
  print("<br>")
  print_data(result)
  htmlBottom()




#con.commit()
#cur.close()
#con.close()
print("<br>")

#print("the connection is closed")


print("""<button><a href='enter_url.html'>Another Result</a></button>""")