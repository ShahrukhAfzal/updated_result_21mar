#!/home/shah/yes/bin/python


print("Content-Type: text/HTML")
print()

print("Importing mysql-connector ")

import mysql.connector

con = mysql.connector.connect(user='root', password='', host='localhost', database='result_demo')
cur = con.cursor()
print("Connection Success")
# cur.execute("select USERNAME,ROLE from user")
#SC = SubjectCode
#SE = SubjectExternalMarks
#ECP = ExternalCarry
#SI = SubjectInternal
#ICP = InternalCarry
cur.execute("""
    CREATE TABLE IF NOT EXISTS result_master_table_demo (
    ROLL_NO INT(10) ,
    SEM INT(1) ,
    SECTION CHAR(1),

    SC1 VARCHAR(10),
    SE1 VARCHAR(3) DEFAULT 0,
    ECP1 INT(1) DEFAULT 0,
    SI1 VARCHAR(3) DEFAULT 0,
    ICP1 INT(1) DEFAULT 0,

    SC2 VARCHAR(10),
    SE2 VARCHAR(3) DEFAULT 0,
    ECP2 INT(1) DEFAULT 0,
    SI2 VARCHAR(3) DEFAULT 0,
    ICP2 INT(1) DEFAULT 0,

    SC3 VARCHAR(10),
    SE3 VARCHAR(3) DEFAULT 0,
    ECP3 INT(1) DEFAULT 0,
    SI3 VARCHAR(3) DEFAULT 0,
    ICP3 INT(1) DEFAULT 0,

    SC4 VARCHAR(10),
    SE4 VARCHAR(3) DEFAULT 0,
    ECP4 INT(1) DEFAULT 0,
    SI4 VARCHAR(3) DEFAULT 0,
    ICP4 INT(1) DEFAULT 0,

    SC5 VARCHAR(10),
    SE5 VARCHAR(3) DEFAULT 0,
    ECP5 INT(1) DEFAULT 0,
    SI5 VARCHAR(3) DEFAULT 0,
    ICP5 INT(1) DEFAULT 0,

    SC6 VARCHAR(10),
    SE6 VARCHAR(3) DEFAULT 0,
    ECP6 INT(1) DEFAULT 0,
    SI6 VARCHAR(3) DEFAULT 0,
    ICP6 INT(1) DEFAULT 0,

    LBC1 VARCHAR(10) , 
    LBE1 VARCHAR(3) DEFAULT 0,
    EBCP1 INT(1) DEFAULT 0,
    LBI1 VARCHAR(3) DEFAULT 0,
    IBCP1 INT(1) DEFAULT 0,


    LBC2 VARCHAR(10),
    LBE2 VARCHAR(3) DEFAULT 0,
    EBCP2 INT(1) DEFAULT 0,
    LBI2 VARCHAR(3) DEFAULT 0,
    IBCP2 INT(1) DEFAULT 0,


    LBC3 VARCHAR(10),
    LBE3 VARCHAR(3) DEFAULT 0,
    EBCP3 INT(1) DEFAULT 0,
    LBI3 VARCHAR(3) DEFAULT 0,
    IBCP3 INT(1) DEFAULT 0,

    LBC4 VARCHAR(10),
    LBE4 VARCHAR(3) DEFAULT 0,
    EBCP4 INT(1) DEFAULT 0,
    LBI4 VARCHAR(3) DEFAULT 0,
    IBCP4 INT(1) DEFAULT 0,

    LAST_UPDATED TIMESTAMP,
    PRIMARY KEY (ROLL_NO,SEM)
)   
""")
#LBCn =LabCode nTH SUBJECT
#LBEn = LabExternalMarks
#EBCPn = CarryPaperExternalLab
#LBIn = LabInternal
#IBCPn = CarryLabInternal
print("succesfully created table")