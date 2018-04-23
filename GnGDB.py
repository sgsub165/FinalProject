import sqlite3

###function to create table
##def createTable():
##    try:
##        conn = sqlite3.connect("contacts.db")  #connect to the DB file
##        c = conn.cursor()   #use for mult row fetch
##        #sqllite3 statement to create table
##        sqlStatement=('''CREATE TABLE IF NOT EXISTS StephenG
##                    (cid integer primary key not null,
##                    NAME text not null,
##                    PHONE text not null);''')
##        conn.execute(sqlStatement)  #execute the sql statement above
##        print("Table StephenG created successfully in the contacts database.\n\n")
##        #check to determine if records exist in table
##        #pulling from contact list
##        c.execute("Select * from StephenG")
##        data = c.fetchone()
##        c.close()
##        if data is None:
##            print("\nRecords do not exist in the DB table" \
##            "\nRecords will be added from the original contact list")
##            for name, phone in contactlist:
##                insertContact(name,phone)
##            print("\nRecords have been successfully inserted into table" \
##                  " StephenG.")
##        else:
##            print("\nRecords exist in database")
##    except sqlite3.OperationalError:
##        print("\nError")
##
#function to insert contact record data into the DB file
def insertContact(name,phone):
    try:
        conn = sqlite3.connect("contacts.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to insert contact record data into the DB file table
        sqlStatement=("INSERT INTO StephenG"
             "(name,phone)"
             "values(?,?)")
        data = (name,phone)
        c.execute(sqlStatement,data)  #execute the sql statement above
        conn.commit()
        conn.close()
    except Exception:
        print("\nError","Please enter a contact name to add")
    
def updateContacts(name,phone,cid):
    try:
        conn = sqlite3.connect("contacts.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to update contact record data in the DB file table
        sqlStatement = ("UPDATE StephenG SET name=?, phone=? WHERE cid=?;")
        c.execute(sqlStatement,(name,phone,cid))  #execute the sql statement above
        conn.commit()
        c.close
        conn.close
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

def deleteContact(cid):
    try:
        conn = sqlite3.connect("contacts.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to delete contact record from the DB file table
        sqlStatement = ("DELETE FROM StephenG WHERE cid = ?;")
        data = str(cid)
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
