import sqlite3

#THIS ONE WORKS 42520182200
def readRecordsDA(*args):
    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file table
    cursor = conn.cursor()
    #sqllite3 statement to query all records from the DB file table
    sqlStatement = ('''SELECT d.lname DOCTOR, dt.date DATE, st.hour_of_day START_TIME, ia.is_available_val AVAILABILITY
                    FROM Doctor d
                    INNER JOIN DoctorAvailability da
                    ON da.doctor_id = d.doctor_id
                    INNER JOIN StartTime st
                    ON da.start_time_id = st.start_time_id
                    INNER JOIN IsAvailable ia
                    ON da.is_available_id = ia.is_available_id
                    INNER JOIN Date dt
                    ON da.date_id = dt.date_id
                    WHERE ia.is_available_id = 1 AND d.doctor_id = (?) ;''')
    data = str(args[0])
    cursor.execute(sqlStatement,data)  #execute the sql statement above
    sqlOutput = cursor.fetchall()  #fetch all records and prep it for returning to the calling function
    cursor.close()
    conn.close
    print(sqlOutput)
    return sqlOutput  #return fetched records

#readRecordsDA(4)

################################################################################################


#THIS ONE WORKS 42520182200
#function to insert contact record data into the DB file
def insertRecord(*args):

    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file
    c = conn.cursor()
    #sqllite3 statement to insert contact record data into the DB file table
    sqlStatement=("INSERT INTO " + args[0] +
         "(fname,lname)"
         "values(?,?)")
    data = (args[1],args[2])
    c.execute(sqlStatement,data)  #execute the sql statement above
    conn.commit()
    conn.close()

#insertRecord("Patient","Bill","Withers")

################################################################################################

#THIS ONE WORKS 42520182200        
def deleteRecord(*args):
    table = args[0]
    table_id = args[1]
    pid = args[2]
    try:
        conn = sqlite3.connect("GnGMedicalGroupIP.db")
        c = conn.cursor()
        sqlStatement = ("DELETE FROM " + table + " WHERE " + table_id + " = ?;")
        data = str(pid)
        c.execute(sqlStatement,(data,))  #execute the sql statement above
        conn.commit()
        c.close()
        conn.close()
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")


#deleteRecord("Patient","patient_id",13)

###############################################################################################

def readRecordSpecific(*args):
    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file table
    try:
        cursor = conn.cursor()
        #sqllite3 statement to query all records from the DB file table
        sqlStatement = ("SELECT " + args[1] + "," + args[2] + " FROM " + args[0] + ";")
        cursor.execute(sqlStatement)  #execute the sql statement above
        sqlOutput = cursor.fetchall()  #fetch all records and prep it for returning to the calling function
        cursor.close()
        conn.close
        print(sqlOutput)
        return sqlOutput  #return fetched records
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

#readRecordSpecific("User","fname","lname")

##############################################################################################

def readRecord(*args):
    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file table

    cursor = conn.cursor()
    #sqllite3 statement to query all records from the DB file table
    sqlStatement = ("SELECT * FROM " + args[0] + " WHERE " + args[1] + " = '" + args[2] + "';")
    cursor.execute(sqlStatement)  #execute the sql statement above
    sqlOutput = cursor.fetchall()  #fetch all records and prep it for returning to the calling function
    cursor.close()
    conn.close
    print(sqlOutput)
    return sqlOutput  #return fetched records

#readRecord("User","lname","Bishop")

###############################################################################################


#testTable("Doctor")

#testTable("Doctor")

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


#function to create table
def testTable(*args):
    table = args[0]
    print(table)
    conn = sqlite3.connect("GnGMedicalGroup.db")  #connect to the DB file
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
