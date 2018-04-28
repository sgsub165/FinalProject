import sqlite3

#function to update records that have 4 fields
def updateRecordFourFields(*args):
    #try:
    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file
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
    #except sqlite3.OperationalError:
        #print("\nError: Something is wrong with the DB file.")

#updateRecord1("User","uid","ctaylor","password","ctaylor1","fname","Craig","lname","Taylor","user_id","9")

###############################################################################
#function to insert record with four fields
def insertRecord(*args):

    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file
    c = conn.cursor()
    #sqllite3 statement to insert contact record data into the DB file table
    sqlStatement=("INSERT INTO " + args[0] +
         "(uid,password,fname,lname)"
         "values(?,?,?,?)")
    data = (args[1],args[2],args[3],args[4])
    c.execute(sqlStatement,data)  #execute the sql statement above
    print(sqlStatement)
    print(data)
    conn.commit()
    conn.close()

#insertRecord("User","bwithers","bwithers1","Bill","Withers")

#################################################################################
#function to read records from a specified table passed from the calling function
def readRecord(*args):
    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file table

    cursor = conn.cursor()
    #sqllite3 statement to query all records from the DB file table
    sqlStatement = ("SELECT * FROM " + args[0] + ";")
    cursor.execute(sqlStatement)  #execute the sql statement above
    sqlOutput = cursor.fetchall()  #fetch all records and prep it for returning to the calling function
    cursor.close()
    conn.close
    print(sqlOutput)
    return sqlOutput  #return fetched records

#readRecord("User")

#######################################################################
#function to create appoint record and update the doc availability to block
def createAppointmentRecord(patient_id,doctor_id,medical_condition_id,date_id,start_time_id):
    #try:
    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file
    c = conn.cursor()
    sqlStatement1 = ("UPDATE Appointment SET patient_id = ?, doctor_id = ?, medical_condition_id = ?, appointment_status_id = 1 WHERE date_id = ? AND start_time_id = ?;")
    c.execute(sqlStatement1,(patient_id,doctor_id,medical_condition_id,date_id,start_time_id))  #execute the sql statement above
    print(sqlStatement1)
    sqlStatement2 = ("UPDATE DoctorAvailability SET is_available_id = 2 WHERE doctor_id = ? AND date_id = ? AND start_time_id = ?;")
    c.execute(sqlStatement2,(doctor_id,date_id,start_time_id))
    print(sqlStatement2)
    conn.commit()
    c.close
    conn.close
    #except sqlite3.OperationalError:
        #print("\nError: Something is wrong with the DB file.")


#createAppointmentRecord(8,1,8,1,1)

#############################################################################
#function to show all records
def showAppointmentRecordsAll():

    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file
    c = conn.cursor()
    sqlStatement = ('''SELECT (p.fname || ' ' || p.lname), doc.lname, dat.date,
                    stm.hour_of_day, mc.condition_name, aptst.appointment_status     
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

#showAppointmentRecordsAll()
####################################################################################
#function to show appointment records per doctor
def showAppointmentRecordsDoc(doctor_id):

    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file
    c = conn.cursor()
    sqlStatement = ('''SELECT (p.fname || ' ' || p.lname), doc.lname, dat.date,
                    stm.hour_of_day, mc.condition_name, aptst.appointment_status      
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

#showAppointmentRecordsDoc(1)

####################################################################################
#function to show appointments per patient
def showAppointmentRecordsPatient(patient_id):

    conn = sqlite3.connect("GnGMedicalGroupIP.db")  #connect to the DB file
    c = conn.cursor()
    sqlStatement = ('''SELECT (p.fname || ' ' || p.lname), doc.lname, dat.date,
                    stm.hour_of_day, mc.condition_name, aptst.appointment_status      
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

#showAppointmentRecordsPatient(6)

