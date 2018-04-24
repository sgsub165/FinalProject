import sqlite3

#function to create table
def testTable():
    conn = sqlite3.connect("GnGMedicalGroup.DB")  #connect to the DB file
    c = conn.cursor()   #use for mult row fetch
    #sqllite3 statement to create table
    sqlStatement=('''SELECT * FROM Doctor''')
    conn.execute(sqlStatement)  #execute the sql statement above
    print("Hello\n")
    #check to determine if records exist in table
    #pulling from contact list
    c.execute("Select * from Doctor")
    data = c.fetchone()
    print(data)
    c.close()

#function to insert contact record data into the DB file
def insertDoctor(fname,lname):
    conn = sqlite3.connect("GnGMedicalGroup.db")  #connect to the DB file
    c = conn.cursor()
    #sqllite3 statement to insert contact record data into the DB file table
    sqlStatement=("INSERT INTO Doctor"
         "(fname,lname)"
         "values(?,?)")
    data = (fname,lname)
    c.execute(sqlStatement,data)  #execute the sql statement above
    conn.commit()
    conn.close()
    
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

def deleteDoctor(pid):
    try:
        conn = sqlite3.connect("contacts.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to delete contact record from the DB file table
        sqlStatement = ("DELETE FROM Doctor WHERE pid = ?;")
        data = str(pid)
        c.execute(sqlStatement,(data,))  #execute the sql statement above
        conn.commit()
        c.close()
        conn.close()
    except:
        print("\nError>> An Exception has occurred while attempting to delete a record!\n")
        conn.rollback()
   
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

#insertDoctor("John","Kelley")
testTable()
