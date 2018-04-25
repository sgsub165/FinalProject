import sqlite3

#function to create table
def testTable(*args):
    table = args[0]
    print(table)
    conn = sqlite3.connect("GnGMedicalGroup.DB")  #connect to the DB file
    c = conn.cursor()   #use for mult row fetch
    #sqllite3 statement to create table
    sqlStatement=("SELECT * FROM " + table + ";")
    conn.execute(sqlStatement)  #execute the sql statement above
    print("Hello\n")
    #check to determine if records exist in table
    #pulling from contact list
    c.execute("SELECT * FROM " + table + ";")
    data = c.fetchone()
    print(data)
    c.close()

#function to insert contact record data into the DB file
def insertRecord(*args):
    table = args[0]
    arg1 = args[1]
    arg2 = args[2]
    try:
        conn = sqlite3.connect("GnGMedicalGroup.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to insert contact record data into the DB file table
        sqlStatement=("INSERT INTO " + table + "(arg1,arg2)"
         "values(?,?)")
        data = (arg1,arg2)
        c.execute(sqlStatement,data)  #execute the sql statement above
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")    

def deleteRecord(*args):
    table = args[0]
    table_id = args[1]
    pid = args[2]
    try:
        conn = sqlite3.connect("GnGMedicalGroup.db")
        c = conn.cursor()
        sqlStatement = ("DELETE FROM " + table + " WHERE " + table_id + " = ?;")
        data = str(pid)
        c.execute(sqlStatement,(data,))  #execute the sql statement above
        conn.commit()
        c.close()
        conn.close()
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

def updateContacts(name,phone,pid):
    try:
        conn = sqlite3.connect("contacts.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to update contact record data in the DB file table
        sqlStatement = ("UPDATE StephenG SET name=?, phone=? WHERE pid=?;")
        c.execute(sqlStatement,(name,phone,pid))  #execute the sql statement above
        conn.commit()
        c.close
        conn.close
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

   
#insertRecord("Doctor","Bill","Withers")
testTable("Doctor")
deleteRecord("Doctor","doctor_id",18)
testTable("Doctor")

def updateContacts(name,phone,pid):
    try:
        conn = sqlite3.connect("contacts.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to update contact record data in the DB file table
        sqlStatement = ("UPDATE StephenG SET name=?, phone=? WHERE pid=?;")
        c.execute(sqlStatement,(name,phone,pid))  #execute the sql statement above
        conn.commit()
        c.close
        conn.close
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")


def readContacts():
    conn = sqlite3.connect("contacts.db")  #connect to the DB file table
    try:
        cursor = conn.cursor()
        #sqllite3 statement to query all records from the DB file table
        sqlStatement = ("SELECT * FROM StephenG")
        cursor.execute(sqlStatement)  #execute the sql statement above
        sqlOutput = cursor.fetchall()  #fetch all records and prep it for returning to the calling function
        cursor.close()
        conn.close
        return sqlOutput  #return fetched records
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")
