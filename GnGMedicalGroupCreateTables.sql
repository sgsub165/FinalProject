DROP TABLE Doctor;
DROP TABLE Nurse;
DROP TABLE Appointment;
DROP TABLE Appointment_Status;
DROP TABLE AppointmentStatusHistory;
DROP TABLE DoctorAvailability;
DROP TABLE DoctorSpecialty;
DROP TABLE MedicalProcedure;
DROP TABLE NurseAvailability;
DROP TABLE NurseSpecialty;
DROP TABLE Patient;
DROP TABLE Specialty;

CREATE TABLE Doctor (
    doctor_id INTEGER      CONSTRAINT pk_doctor_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                           NOT NULL ON CONFLICT ROLLBACK,
    fname     VARCHAR (30) NOT NULL ON CONFLICT ROLLBACK,
    lname     VARCHAR (30) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE Nurse (
    nurse_id INTEGER      CONSTRAINT pk_nurse_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                          NOT NULL ON CONFLICT ROLLBACK,
    fname    VARCHAR (30) NOT NULL ON CONFLICT ROLLBACK,
    lname    VARCHAR (30) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE Specialty (
    specialty_id   INTEGER      CONSTRAINT pk_specialty_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                NOT NULL,
    specialty_name VARCHAR (45) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE Patient (
    patient_id INTEGER      CONSTRAINT pk_patient_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                            NOT NULL,
    fname      VARCHAR (30) NOT NULL ON CONFLICT ROLLBACK,
    lname      VARCHAR (30) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE MedicalProcedure (
    procedure_id   INTEGER      CONSTRAINT pk_procedure_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                NOT NULL ON CONFLICT ROLLBACK,
    procedure_name VARCHAR (45) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE Appointment_Status (
    appointment_status_id INTEGER      CONSTRAINT pk_appointment_status_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                       NOT NULL ON CONFLICT ROLLBACK,
    appointment_status    VARCHAR (16) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE Appointment (
    appointment_id            INTEGER CONSTRAINT pk_appointment_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                      NOT NULL ON CONFLICT ROLLBACK,
    patient_id                INTEGER CONSTRAINT fk_patient_id REFERENCES Patient (patient_id) 
                                      NOT NULL ON CONFLICT ROLLBACK,
    doctor_id                 INTEGER CONSTRAINT fk_doctor_id REFERENCES Doctor (doctor_id) 
                                      NOT NULL ON CONFLICT ROLLBACK,
    nurse_id                  INTEGER CONSTRAINT fk_nurse_id REFERENCES Nurse (nurse_id) 
                                      NOT NULL ON CONFLICT ROLLBACK,
    start_time                TIME    NOT NULL ON CONFLICT ABORT,
    end_time                  TIME    NOT NULL ON CONFLICT ABORT,
    appointment_status_id     INTEGER CONSTRAINT fk_appointment_status_id REFERENCES Appointment_Status (appointment_status_id) 
                                      NOT NULL ON CONFLICT ROLLBACK,
    appointment_creation_date DATE    NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE AppointmentStatusHistory (
    appointment_history_id INTEGER     CONSTRAINT pk_appointment_history_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                       NOT NULL ON CONFLICT ROLLBACK,
    appointment_id         INTEGER     CONSTRAINT fk_appointment_id REFERENCES Appointment (appointment_id) 
                                       NOT NULL ON CONFLICT ROLLBACK,
    appointment_status_id  INTEGER     CONSTRAINT fk1_appointment_status_id REFERENCES Appointment_Status (appointment_status_id) 
                                       NOT NULL,
    details                TEXT (1024) 
);

CREATE TABLE DoctorSpecialty (
    doctor_specialty_id INTEGER CONSTRAINT pk_doctor_specialty_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                NOT NULL ON CONFLICT ROLLBACK,
    doctor_id           INTEGER CONSTRAINT fk1_doctor_id REFERENCES Doctor (doctor_id) 
                                NOT NULL ON CONFLICT ROLLBACK,
    specialty_id        INTEGER CONSTRAINT fk_specialty_id REFERENCES Specialty (specialty_id) 
                                NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE DoctorAvailability (
    doctor_availability_id INTEGER  CONSTRAINT pk_doctor_availability_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                    NOT NULL ON CONFLICT ROLLBACK,
    doctor_id              INTEGER  CONSTRAINT fk2_doctor_id REFERENCES Doctor (doctor_id) 
                                    NOT NULL ON CONFLICT ROLLBACK,
    date_available         DATE,
    start_time             TIME     NOT NULL ON CONFLICT ROLLBACK,
    end_time               TIME,
    is_available           CHAR (1) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE NurseSpecialty (
    nurse_specialty_id INTEGER CONSTRAINT pk_nurse_specialty_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                               NOT NULL ON CONFLICT ROLLBACK,
    nurse_id           INTEGER CONSTRAINT fk1_nurse_id REFERENCES Nurse (nurse_id) 
                               NOT NULL ON CONFLICT ROLLBACK,
    specialty_id       INTEGER CONSTRAINT fk1_specialty_id REFERENCES Specialty (specialty_id) 
                               NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE NurseAvailability (
    nurse_availability_id INTEGER  CONSTRAINT pk_nurse_availability_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                   NOT NULL ON CONFLICT ROLLBACK,
    nurse_id              INTEGER  CONSTRAINT fk2_nurse_id REFERENCES Nurse (nurse_id) 
                                   NOT NULL ON CONFLICT ROLLBACK,
    date_available        DATE     NOT NULL ON CONFLICT ROLLBACK,
    start_time            TIME     NOT NULL ON CONFLICT ROLLBACK,
    end_time              DATE     NOT NULL ON CONFLICT ROLLBACK,
    is_available          CHAR (1) 
);
