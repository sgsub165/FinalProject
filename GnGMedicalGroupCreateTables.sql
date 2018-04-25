DROP TABLE IF EXISTS Doctor;
DROP TABLE IF EXISTS Nurse;
DROP TABLE if EXISTS Patient;
DROP TABLE IF EXISTS MedicalProcedure;
DROP TABLE IF EXISTS AppointmentStatus;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS DayOfWeek;
DROP TABLE IF EXISTS StartTime;
DROP TABLE IF EXISTS IsAvailable;
DROP TABLE IF EXISTS DoctorAvailability;
DROP TABLE IF EXISTS NurseAvailability;
DROP TABLE IF EXISTS Appointment;
DROP TABLE IF EXISTS AppointmentStatusHistory;

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

CREATE TABLE AppointmentStatus (
    appointment_status_id INTEGER      CONSTRAINT pk_appointment_status_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                       NOT NULL ON CONFLICT ROLLBACK,
    appointment_status    VARCHAR (16) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE User (
    user_id  INTEGER      CONSTRAINT pk_user_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                          NOT NULL ON CONFLICT ROLLBACK,
    uid      VARCHAR (30) NOT NULL ON CONFLICT ROLLBACK,
    password VARCHAR (30) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE DayOfWeek (
    day_of_week_id INTEGER     CONSTRAINT pk_day_of_week_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                               NOT NULL,
    day_of_week    VARCHAR (8) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE StartTime (
    start_time_id INTEGER      CONSTRAINT pk_start_time_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                               NOT NULL ON CONFLICT ROLLBACK,
    hour_of_day   VARCHAR (10) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE IsAvailable (
    is_available_id  INTEGER  CONSTRAINT pk_is_available_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                              NOT NULL ON CONFLICT ROLLBACK,
    is_available_val CHAR (1) NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE DoctorAvailability (
    doctor_availability_id INTEGER      CONSTRAINT pk_doctor_availability_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                        NOT NULL ON CONFLICT ROLLBACK,
    doctor_id              INTEGER      CONSTRAINT fk2_doctor_id REFERENCES Doctor (doctor_id) 
                                        NOT NULL ON CONFLICT ROLLBACK,
    day_of_week_id         VARCHAR (10) CONSTRAINT fk_day_of_week_id REFERENCES DayOfWeek (day_of_week_id) 
                                        NOT NULL,
    start_time_id          VARCHAR (8)  NOT NULL ON CONFLICT ROLLBACK
                                        CONSTRAINT fk_start_time_id REFERENCES StartTime (start_time_id),
    is_available_id        CHAR (1)     NOT NULL ON CONFLICT ROLLBACK
                                        CONSTRAINT fk_is_available_id REFERENCES IsAvailable (is_available_id) 
);

CREATE TABLE NurseAvailability (
    nurse_availability_id INTEGER      CONSTRAINT pk_nurse_availability_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                       NOT NULL ON CONFLICT ROLLBACK,
    nurse_id              INTEGER      CONSTRAINT fk2_nurse_id REFERENCES Nurse (nurse_id) 
                                       NOT NULL ON CONFLICT ROLLBACK,
    day_of_week_id        VARCHAR (10) NOT NULL ON CONFLICT ROLLBACK
                                       CONSTRAINT fk1_day_of_week_id REFERENCES DayOfWeek (day_of_week_id),
    start_time_id         VARCHAR (8)  NOT NULL ON CONFLICT ROLLBACK
                                       CONSTRAINT fk_start_time_id REFERENCES StartTime (start_time_id),
    is_available_id       CHAR (1)     CONSTRAINT fk_is_available_id REFERENCES IsAvailable (is_available_id) 
                                       NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE Appointment (
    appointment_id            INTEGER      CONSTRAINT pk_appointment_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                           NOT NULL ON CONFLICT ROLLBACK,
    patient_id                INTEGER      CONSTRAINT fk_patient_id REFERENCES Patient (patient_id) 
                                           NOT NULL ON CONFLICT ROLLBACK,
    doctor_id                 INTEGER      CONSTRAINT fk_doctor_id REFERENCES Doctor (doctor_id) 
                                           NOT NULL ON CONFLICT ROLLBACK,
    nurse_id                  INTEGER      CONSTRAINT fk_nurse_id REFERENCES Nurse (nurse_id) 
                                           NOT NULL ON CONFLICT ROLLBACK,
    day_of_week_id            VARCHAR (10) NOT NULL ON CONFLICT ABORT
                                           CONSTRAINT fk2_day_of_week_id REFERENCES DayOfWeek (day_of_week_id),
    start_time_id             VARCHAR (8)  NOT NULL ON CONFLICT ABORT
                                           CONSTRAINT fk_start_time_id REFERENCES StartTime (start_time_id),
    appointment_status_id     INTEGER      CONSTRAINT fk_appointment_status_id REFERENCES AppointmentStatus (appointment_status_id) 
                                           NOT NULL ON CONFLICT ROLLBACK,
    appointment_creation_date DATE         NOT NULL ON CONFLICT ROLLBACK
);

CREATE TABLE AppointmentStatusHistory (
    appointment_history_id INTEGER     CONSTRAINT pk_appointment_history_id PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                       NOT NULL ON CONFLICT ROLLBACK,
    appointment_id         INTEGER     CONSTRAINT fk_appointment_id REFERENCES Appointment
                                       NOT NULL ON CONFLICT ROLLBACK,
    appointment_status_id  INTEGER     CONSTRAINT fk1_appointment_status_id REFERENCES Appointment_Status (appointment_status_id) 
                                       NOT NULL,
    details                TEXT (1024) 
);
