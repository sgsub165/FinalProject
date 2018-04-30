import sqlite3
#
#This file contains the python functions to perform sql operations on the database.
#
#Author: Stephen Griffith
#Co-Author: Paul Gierzynski
#ITD-813
#Final Project
#04/29/2018
#
######################################################################################
#function to insert contact record data into the DB file
def insertRecord(*args):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to insert contact record data into the DB file table
        sqlStatement=("INSERT INTO " + args[0] +
             "(fname,lname)"
             "values(?,?)")
        data = (args[1],args[2])
        c.execute(sqlStatement,data)  #execute the sql statement above
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

##########################################################################################
def insertRecord4F(*args):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to insert contact record data into the DB file table
        sqlStatement=("INSERT INTO " + args[0] +
             "(uid,password,fname,lname)"
             "values(?,?,?,?)")
        data = (args[1],args[2],args[3],args[4])
        c.execute(sqlStatement,data)  #execute the sql statement above
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

################################################################################################
def deleteRecord(*args):
    table = args[0]
    table_id = args[1]
    pid = args[2]
    try:
        conn = sqlite3.connect("GnGDB.db")
        c = conn.cursor()
        sqlStatement = ("DELETE FROM " + table + " WHERE " + table_id + " = ?;")
        data = str(pid)
        c.execute(sqlStatement,(data,))  #execute the sql statement above
        conn.commit()
        c.close()
        conn.close()
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

###############################################################################################
def readRecordSpecific(*args):
    conn = sqlite3.connect("GnGDB.db")  #connect to the DB file table
    try:
        cursor = conn.cursor()
        #sqllite3 statement to query all records from the DB file table
        sqlStatement = ("SELECT " + args[1] + "," + args[2] + " FROM " + args[0] + ";")
        cursor.execute(sqlStatement)  #execute the sql statement above
        sqlOutput = cursor.fetchall()  #fetch all records and prep it for returning to the calling function
        cursor.close()
        conn.close
        #print(sqlOutput)
        return sqlOutput  #return fetched records
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

##############################################################################################
def readRecordAll(*args):
    conn = sqlite3.connect("GnGDB.db")  #connect to the DB file table
    try:
        cursor = conn.cursor()
        #sqllite3 statement to query all records from the DB file table
        sqlStatement = ("SELECT * FROM " + args[0] + ';')
        cursor.execute(sqlStatement)  #execute the sql statement above
        sqlOutput = cursor.fetchall()  #fetch all records and prep it for returning to the calling function
        cursor.close()
        conn.close
        #print(sqlOutput)
        return sqlOutput  #return fetched records
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

##############################################################################################
def updateRecord2F(*args):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        sqlStatement = ("UPDATE " + args[0] + " SET "
                        + args[1] + " = '" + args[2] + "', "
                        + args[3] + " = '" + args[4] +
                        "' WHERE " + args[5] + " = '" + args[6] + "';")
        c.execute(sqlStatement)  #execute the sql statement above
        conn.commit()
        c.close
        conn.close
        print(sqlStatement)
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

###############################################################################################
def updateRecord4F(*args):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        #sqllite3 statement to update contact record data in the DB file table
        sqlStatement = ("UPDATE " + args[0] + " SET "
                        + args[1] + " = '" + args[2] + "', "
                        + args[3] + " = '" + args[4] + "', "
                        + args[5] + " = '" + args[6] + "', "
                        + args[7] + " = '" + args[8] +
                        "' WHERE " + args[9] + " = '" + args[10] + "';")
        c.execute(sqlStatement)  #execute the sql statement above
        print(sqlStatement)
        conn.commit()
        c.close
        conn.close
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

##################################################################################################
#function to read records from a specified table passed from the calling function
def readRecord(*args):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file table
        cursor = conn.cursor()
        #sqllite3 statement to query all records from the DB file table
        sqlStatement = ("SELECT * FROM " + args[0] + ";")
        cursor.execute(sqlStatement)  #execute the sql statement above
        sqlOutput = cursor.fetchall()  #fetch all records and prep it for returning to the calling function
        cursor.close()
        conn.close
        print(sqlOutput)
        return sqlOutput  #return fetched records
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

#######################################################################
#function to create appoint record and update the doc availability to block
def createAppointmentRecord(patient_id,doctor_id,medical_condition_id,date_id,start_time_id):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        sqlStatement1 = ('''INSERT INTO Appointment (appointment_id, patient_id,
                            doctor_id, date_id, start_time_id, medical_condition_id,
                            appointment_status_id, appt_creation_date, appt_cancel_date, appt_cmplt_date)
                            VALUES (NULL,?,?,?,?,?,1,NULL,NULL,NULL);''')
        c.execute(sqlStatement1,(patient_id,doctor_id,medical_condition_id,date_id,start_time_id))  #execute the sql statement above
        sqlStatement2 = ("UPDATE DoctorAvailability SET is_available_id = 2 WHERE doctor_id = ? AND date_id = ? AND start_time_id = ?;")
        c.execute(sqlStatement2,(doctor_id,date_id,start_time_id))
        print(sqlStatement2)
        conn.commit()
        c.close
        conn.close
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

#############################################################################
#function to show all records
def showAppointmentRecordsAll():
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        sqlStatement = ('''SELECT (p.fname || ' ' || p.lname), doc.lname, dat.date,
                        stm.hour_of_day, mc.condition_name, aptst.appointment_status,
                        dat.date_id, stm.start_time_id     
                        FROM Appointment apt
                        INNER JOIN Patient p
                        ON apt.patient_id = p.patient_id
                        INNER JOIN Doctor doc
                        ON apt.doctor_id = doc.doctor_id
                        INNER JOIN MedicalCondition mc
                        ON apt.medical_condition_id = mc.condition_id
                        INNER JOIN Date dat
                        ON apt.date_id = dat.date_id
                        INNER JOIN StartTime stm
                        ON apt.start_time_id = stm.start_time_id
                        INNER JOIN AppointmentStatus aptst
                        ON apt.appointment_status_id = aptst.appointment_status_id;''')
        c.execute(sqlStatement)
        sqlOutput = c.fetchall()
        print(sqlOutput)
        conn.commit()
        c.close
        conn.close
        return sqlOutput
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

####################################################################################
#function to show appointment records per doctor
def showAppointmentRecordsDoc(doctor_id):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        sqlStatement = ('''SELECT (p.fname || ' ' || p.lname), doc.lname, dat.date,
                        stm.hour_of_day, mc.condition_name, aptst.appointment_status,
                        dat.date_id, stm.start_time_id
                        FROM Appointment apt
                        INNER JOIN Patient p
                        ON apt.patient_id = p.patient_id
                        INNER JOIN Doctor doc
                        ON apt.doctor_id = doc.doctor_id
                        INNER JOIN MedicalCondition mc
                        ON apt.medical_condition_id = mc.condition_id
                        INNER JOIN Date dat
                        ON apt.date_id = dat.date_id
                        INNER JOIN StartTime stm
                        ON apt.start_time_id = stm.start_time_id
                        INNER JOIN AppointmentStatus aptst
                        ON apt.appointment_status_id = aptst.appointment_status_id
                        WHERE apt.doctor_id = ?;''')
        data = str(doctor_id)
        c.execute(sqlStatement,(data,))
        sqlOutput = c.fetchall()
        print(sqlOutput)
        conn.commit()
        c.close
        conn.close
        return sqlOutput
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

####################################################################################
#function to show appointments per patient
def showAppointmentRecordsPatient(patient_id):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        sqlStatement = ('''SELECT (p.fname || ' ' || p.lname), doc.lname, dat.date,
                        stm.hour_of_day, mc.condition_name, aptst.appointment_status,
                        dat.date_id, stm.start_time_id      
                        FROM Appointment apt
                        INNER JOIN Patient p
                        ON apt.patient_id = p.patient_id
                        INNER JOIN Doctor doc
                        ON apt.doctor_id = doc.doctor_id
                        INNER JOIN MedicalCondition mc
                        ON apt.medical_condition_id = mc.condition_id
                        INNER JOIN Date dat
                        ON apt.date_id = dat.date_id
                        INNER JOIN StartTime stm
                        ON apt.start_time_id = stm.start_time_id
                        INNER JOIN AppointmentStatus aptst
                        ON apt.appointment_status_id = aptst.appointment_status_id
                        WHERE apt.patient_id = ?;''')
        data = str(patient_id)
        c.execute(sqlStatement,(data,))
        sqlOutput = c.fetchall()
        print(sqlOutput)
        conn.commit()
        c.close
        conn.close
        return sqlOutput
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

##################################################################################################
def showDoctorAvailability(doctor_id):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        sqlStatement = ('''SELECT d.lname, dt.date_id, dt.date, st.start_time_id, st.hour_of_day
                        FROM DoctorAvailability da
                        INNER JOIN Doctor d
                        ON da.doctor_id = d.doctor_id
                        INNER JOIN StartTime st
                        ON da.start_time_id = st.start_time_id
                        INNER JOIN IsAvailable ia
                        ON da.is_available_id = ia.is_available_id
                        INNER JOIN Date dt
                        ON da.date_id = dt.date_id
                        WHERE ia.is_available_id = 1 AND d.doctor_id = ?;''')
        data = str(doctor_id)
        c.execute(sqlStatement,(data,))
        sqlOutput = c.fetchall()
        print(sqlOutput)
        conn.commit()
        c.close
        conn.close
        return sqlOutput
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

##################################################################################################
#function to cancel an appointment and update the doctor availability to available
def cancelAppointmentRecord(patient_id,doctor_id,date_id,start_time_id):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        #sql update statement to change the appointment status to cancel
        sqlStatement1 = ('''UPDATE Appointment SET appointment_status_id = 2
                         WHERE patient_id = ? AND date_id = ? AND start_time_id = ?;''')
        c.execute(sqlStatement1,(patient_id, date_id,start_time_id))  #execute the sql statement above
        #print(sqlStatement1)
        #sql update statement to change the doctor availability to available
        sqlStatement2 = ('''UPDATE DoctorAvailability SET is_available_id = 1
                         WHERE doctor_id = ? AND date_id = ? AND start_time_id = ?;''')
        c.execute(sqlStatement2,(doctor_id,date_id,start_time_id))
        #print(sqlStatement2)
        conn.commit()
        c.close
        conn.close
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

##################################################################################################
#function to move the appointment to a terminal completed state
def completeAppointmentRecord(patient_id,date_id,start_time_id):
    try:
        conn = sqlite3.connect("GnGDB.db")  #connect to the DB file
        c = conn.cursor()
        sqlStatement = ('''UPDATE Appointment SET appointment_status_id = 3
                         WHERE patient_id = ? AND date_id = ? AND start_time_id = ?;''')
        c.execute(sqlStatement,(patient_id,date_id,start_time_id))  #execute the sql statement above
        conn.commit()
        c.close
        conn.close
    except sqlite3.OperationalError:
        print("\nError: Something is wrong with the DB file.")

##################################################################################################
#End Of File
##################################################################################################

