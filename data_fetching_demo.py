#!/home/shah/yes/bin/python

print("Content-Type: text/HTML")
print()

print("<h1>This is our coding page\n\n</h1><br><br>")
#print("<h2>This page will be maintained by <mark>Shahrukh Afzal</mark></h2>")

print("<a href='enter_url.html'>Another Result</a>")
print("<br><br>")
print("<br><br>")

print("<a href='index.html'>Home</a>")
print("<br><br>")
print("<br><br>")


import pandas as pd
import cgi

form = cgi.FieldStorage()


url = form.getvalue("url")
section = form.getvalue("section")

print("the student is of section {}".format(section))

data = pd.read_html(url)
print(data[8][0][5][3])
print("data loaded")


def personal_data(arg):
    course = arg[2][2][2]
    name = arg[2][2][4]
    roll_no = arg[2][2][3]
    branch = arg[2][5][2]
    college = arg[2][2][1]
    gender = arg[2][5][5]
    return roll_no, name, branch, gender, course, college


def sem_data(arg):
    a = []
    for i in range(8, len(arg), 7):
        a.append(arg[i])
    for j in range(11, len(arg), 7):
        a.append(arg[j])
    return a



# last modified March 6, 13:25
def final_sem(raw_sem):
    z = []
    sem1 = 0
    sem2 = 0
    sem3 = 0
    sem4 = 0
    sem5 = 0
    sem6 = 0
    sem7 = 0
    sem8 = 0
    for j in range(len(raw_sem) - 1):
        if ((raw_sem[j][0][5][3]) == '1'):
            sem1 = (raw_sem[j])

        elif ((raw_sem[j][0][5][3]) == '2'):
            sem2 = (raw_sem[j])
            #
        elif ((raw_sem[j][0][5][3]) == '3'):
            sem3 = (raw_sem[j])
            # z.append(sem3)
        elif ((raw_sem[j][0][5][3]) == '4'):
            sem4 = (raw_sem[j])
            # z.append(sem4)
        elif ((raw_sem[j][0][5][3]) == '5'):
            sem5 = (raw_sem[j])
            # z.append(sem5)
        elif ((raw_sem[j][0][5][3]) == '6'):
            sem6 = (raw_sem[j])
            # z.append(sem6)
        elif ((raw_sem[j][0][5][3]) == '7'):
            sem7 = (raw_sem[j])
            # z.append(sem7)
        elif ((raw_sem[j][0][5][3]) == '8'):
            sem8 = (raw_sem[j])
            # z.append(sem8)
    try:
        if len(sem1) != 1:
            z.append(sem1)
    except:
        pass
    try:
        if len(sem2) != 1:
            z.append(sem2)
    except:
        pass
    try:
        if len(sem3) != 1:
            z.append(sem3)
    except:
        pass
    try:
        if len(sem4) != 1:
            z.append(sem4)
    except:
        pass
    try:
        if len(sem5) != 1:
            z.append(sem5)
    except:
        pass
    try:
        if len(sem6) != 1:
            z.append(sem6)
    except:
        pass
    try:
        if len(sem7) != 1:
            z.append(sem7)
    except:
        pass
    try:
        if len(sem8) != 1:
            z.append(sem8)
    except:
        pass
    return z


#print("Wait!!! Data is being loaded\n\n")
def na_fill(args):
    for each in args:
        each.fillna(value=0, inplace=True)
    return args


'''
def header(arg):
    i=[]
    for each in arg:
        try:
            each.columns = each.iloc[0]
            each=each[1:]
            i.append(each)
        except:
            pass
    return i  
'''


#print("Wait!!! Data is also being loaded\n\n")
roll_no, name, branch, gender, course, college = personal_data(data)



#sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8 = final_sem(na_fill(sem_data(data)))
#print("Wait!!! Data is being loaded\n\n")
print("<br><br>")
print("<b><mark>", name, "</mark></b>", " whose roll_no is ", "<mark>", roll_no, "</mark>", " is studying ", course, " ", "<mark>", branch, "</mark>", " in ",  college, " college<br><br> ")

#view_back = lambda sem:sem[sem['Grade' or 'Credit']=='F'] #((sem[sem['Credit']=='F']) or (sem[sem['Grade']=='F']) or (sem[sem['Credit']=='0']))

#view_back=lambda sem: sem[0][sem[6]== 'F']  # this code is now only work for the 2017 & later



a=na_fill(sem_data(data))
b=final_sem(a)



'''

print("<br><br>")
print("<br><br>")
try:
    print("Back in semester  <b>1</b>  : \n\n")
    for i in range(0, len(view_back(b[0]))):
        print(i + 1, sep='.')
        print("<mark>",view_back(b[0]).iloc[i],"</mark>")
        print("&nbsp")
        print("&nbsp")
        print("&nbsp")
except:
    pass   

print("<br><br>")
try:
    print("Back in semester  <b>2</b>  : \n\n")
    for i in range(0, len(view_back(b[1]))):
        print(i + 1, sep='.')
        print("<mark>",view_back(b[1]).iloc[i],"</mark>")
        print("&nbsp")
        print("&nbsp")
        print("&nbsp")
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>3</b>  : \n\n")
    for i in range(0, len(view_back(b[2]))):
        print(i+1,sep='.')
        print("<mark>",view_back(b[2]).iloc[i],"</mark>")
        print("&nbsp")
        print("&nbsp")
        print("&nbsp")
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>4</b>  : \n\n")
    for i in range(0, len(view_back(b[3]))):
        print(i + 1, sep='.')
        print("<mark>",view_back(b[3]).iloc[i],"</mark>")
        print("&nbsp")
        print("&nbsp")
        print("&nbsp")
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>5</b>  : \n\n")
    for i in range(0, len(view_back(b[4]))):
        print(i + 1, sep='.')
        print("<mark>",view_back(b[4]).iloc[i],"</mark>")
        print("&nbsp")
        print("&nbsp")
        print("&nbsp")
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>6</b>  : \n\n")
    for i in range(0, len(view_back(b[5]))):
        print(i + 1, sep='.')
        print("<mark>",view_back(b[5]).iloc[i],"</mark>")
        print("&nbsp")
        print("&nbsp")
        print("&nbsp")
except:
    pass  

print("<br><br>")
try:
    print("Back in semester  <b>7</b>  : \n\n")
    for i in range(0, len(view_back(b[6]))):
        print(i + 1, sep='.')
        print("<mark>",view_back(b[6]).iloc[i],"</mark>")
        print("&nbsp")
        print("&nbsp")
        print("&nbsp")
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>8</b>  : \n\n")
    for i in range(0, len(view_back(b[7]))):
        print(i + 1, sep='.')
        print("<mark>",view_back(b[7]).iloc[i],"</mark>")
        print("&nbsp")
        print("&nbsp")
        print("&nbsp")
except:
    pass  
print("<br><br>")

'''

import mysql.connector

con = mysql.connector.connect(user='root', password='', host='localhost', database='result_demo')
cur = con.cursor()
print("Connection Success")


def create_table_master_table():
    cur.execute("""
            CREATE TABLE if not exists MASTER_TABLE
            (
             ROLL_NO varchar(10) NOT NULL,
             SESSION varchar(2) NOT NULL,
             SEMESTER varchar(1) NOT NULL,
             BRANCH_CODE varchar(2) NOT NULL,
             SECTION varchar(5) NOT NULL,
             SUBJECT_CODE varchar(10) DEFAULT '0',
             EXTERNAL varchar(3) DEFAULT '0',
             INTERNAL varchar(3) DEFAULT '0',
             GRADE varchar(3) DEFAULT 'A',
             PRIMARY KEY (ROLL_NO,SUBJECT_CODE)) """)
    con.commit()

print("table created")

def insert_in_master_table(semester, subject_no):
    cur.execute("""insert into MASTER_TABLE
    (
    ROLL_NO, 
    SESSION,
    SEMESTER,
    BRANCH_CODE,
    SECTION,
    SUBJECT_CODE,
    EXTERNAL,
    INTERNAL,
    GRADE) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
                tuple([roll_no,
                       roll_no[:2],  # session
                       semester[0].iloc[2][3:4],#semester value
                       roll_no[5:7],#branch_code
                       section,#manually entered
                       semester[0].iloc[subject_no],  # subject code
                       semester[4].iloc[subject_no],  # external
                       semester[3].iloc[subject_no],  # internal
                       semester[6].iloc[subject_no]  # grade
                       ]))
    con.commit()


def update_data(semester, subject_no):
    cur.execute("""UPDATE MASTER_TABLE 
                SET 
                ROLL_NO = {ROLL_NO}, 
                SESSION = {SESSION},
                SEMESTER= {SEMESTER},
                BRANCH_CODE = {BRANCH_CODE},
                SECTION = {SECTION},
                SUBJECT_CODE ={SUBJECT_CODE},
                EXTERNAL={EXTERNAL},
                INTERNAL ={INTERNAL},
                GRADE ={GRADE}

                WHERE ROLL_NO = {ROLL_NO} AND SEMESTER = {SEMESTER}
                """.format(ROLL_NO=roll_no,
                           SESSION=roll_no[:2],  # session
                           SEMESTER=semester[0].iloc[2][3:4],  # semester value
                           BRANCH_CODE=roll_no[5:7],  # branch_code
                           SECTION=section,  # manually entered
                           SUBJECT_CODE=semester[0].iloc[subject_no],  # subject code
                           EXTERNAL=semester[4].iloc[subject_no],  # external
                           INTERNAL=semester[3].iloc[subject_no],  # internal
                           GRADE=semester[6].iloc[subject_no]))
    con.commit()


print("the functions defined")

#insert_in_master_table(sem2, 1)

def insert_all():
    count =0
    for j in b:
        count+=1
        for i in range(1,len(j)):#for i range(len(sem))
            try:
                #update_data(j, i)
                insert_in_master_table(j,i)
                print("""
                    <script>
                    alert("data successfully entered for sem{}".format(count));
                    </script>
                """)
            except Exception as e:
                print(e)

                #print("Data already exist for sem{}".format(count))

create_table_master_table()
insert_all()


print("Succesfully created table")
#print("<br><h1>{}</h1>".format(flag))
cur.close()
con.close()
print("<hr/>")
print("Connection closed")



print("<button><a href='index.html'>Home</a></button>")






