import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS ICU")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="ICU"
)
mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Doctor (DOC_ID INT NOT NULL, DOC_Fname VARCHAR(255), DOC_Lname VARCHAR(255), DOC_SSN INT, DOC_Email VARCHAR(255), DOC_Password VARCHAR(255), DOC_Specialisation VARCHAR(255), DOC_PhoneNo INT, PRIMARY KEY(DOC_ID), UNIQUE(DOC_SSN))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Nurse (Nurse_ID INT NOT NULL, Nurse_Fname VARCHAR(255), Nurse_Lname VARCHAR(255), Nurse_SSN INT, Nurse_Email VARCHAR(255), Nurse_Password VARCHAR(255), Nurse_PhoneNo INT, PRIMARY KEY(Nurse_ID), UNIQUE(Nurse_SSN))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Patient (PAT_ID INT NOT NULL, PAT_Fname VARCHAR(255), PAT_Lname VARCHAR(255), PAT_SSN INT, PAT_Email VARCHAR(255), PAT_Password VARCHAR(255), PAT_RoomNo INT, PAT_PhoneNo INT, PRIMARY KEY(PAT_ID), UNIQUE(PAT_SSN))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Engineer (ENG_ID INT NOT NULL, ENG_Fname VARCHAR(255), ENG_Lname VARCHAR(255), ENG_SSN INT, ENG_Email VARCHAR(255), ENG_Password VARCHAR(255), ENG_PhoneNo INT, PRIMARY KEY(ENG_ID), UNIQUE(ENG_SSN))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Device (Device_ID INT NOT NULL, Device_Name VARCHAR(255), PRIMARY KEY(Device_ID))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Admin (Admin_ID INT NOT NULL, Admin_SSN INT, Admin_Fname VARCHAR(255), Admin_Lname VARCHAR(255), Admin_Email VARCHAR(255), Admin_Password VARCHAR(255), Admin_PhoneNo INT, PRIMARY KEY(Admin_ID))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS CheckUp (DOC_Code INT NOT NULL, PAT_Code INT NOT NULL, FOREIGN KEY (DOC_Code) REFERENCES Doctor(DOC_ID), FOREIGN KEY (PAT_Code) REFERENCES Patient(PAT_ID))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Cares (Nurse_Code INT NOT NULL, PAT_Code INT NOT NULL, FOREIGN KEY (Nurse_Code) REFERENCES Nurse(Nurse_ID), FOREIGN KEY (PAT_Code) REFERENCES Patient(PAT_ID))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Maintenance (Device_Code INT NOT NULL, ENG_Code INT NOT NULL, FOREIGN KEY (Device_Code) REFERENCES Device(Device_ID), FOREIGN KEY (ENG_Code) REFERENCES Engineer(ENG_ID))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Complain (Comp_No INT NOT NULL AUTO_INCREMENT, PAT_Code INT NOT NULL, Comp_Msg TEXT(20000), FOREIGN KEY (PAT_Code) REFERENCES Patient(PAT_ID) ,PRIMARY KEY (Comp_No))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Medications (Medication_ID INT NOT NULL, Medication_Name VARCHAR(250), Medication_Dose VARCHAR(250), PRIMARY KEY (Medication_ID))")

mycursor.execute("CREATE TABLE IF NOT EXISTS MedRelation (PAT_Code INT NOT NULL, DOC_Code INT NOT NULL, Medication_Code INT NOT NULL, FOREIGN KEY (PAT_Code) REFERENCES Patient(PAT_ID), FOREIGN KEY (DOC_Code) REFERENCES Doctor(DOC_ID), FOREIGN KEY (Medication_Code) REFERENCES Medications(Medication_ID))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Images (Image_ID INTEGER(45) NOT NULL AUTO_INCREMENT, Photo LONGBLOB NOT NULL, PAT_Code INT NOT NULL, DOC_Code INT NOT NULL, DOC_Name VARCHAR(250), Scan_Description VARCHAR(250) NOT NULL, FOREIGN KEY (PAT_Code) REFERENCES Patient(PAT_ID), FOREIGN KEY (DOC_Code) REFERENCES Doctor(DOC_ID), PRIMARY KEY(Image_ID))")


mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

###
sql = "INSERT INTO Admin (Admin_ID, Admin_SSN, Admin_Fname, Admin_Lname, Admin_Email, Admin_Password, Admin_PhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [
    ('1', '29909', 'Mohamed', 'Ahmed',
        'databaseproject110@gmail.com', '12345600', '01096162907'),
    ('2', '2879', 'Mohamed', 'Abdelmonem',
        'mohamed.a.abdelmonem1@gmail.com', '12345600', '01018404411'),
]

mycursor.executemany(sql, val)
mydb.commit()


##
sql = "INSERT INTO Engineer (ENG_ID, ENG_Fname, ENG_Lname, ENG_SSN, ENG_Email, ENG_Password, ENG_PhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [
    ('2000', 'AbdulRahman', 'Hossam', '29907',
     'abdo@yahoo.com', '1616551351', '01147240814'),
    ('2001', 'Ahmed', 'Ragab', '29806',
        'ahmed.rajab1@yahoo.com', 'rajab1165165', '01148711709'),
    ('2002', 'Amira', 'Mahmoud', '29908',
        'amira@yahoo.com', '5252452452', '01111813356'),
    ('2003', 'Youmna', 'Hamdy', '29909',
        'yumna12@yahoo.com', '52245245', '01099895374'),
]

mycursor.executemany(sql, val)
mydb.commit()

###
sql = "INSERT INTO Doctor (DOC_ID, DOC_Fname, DOC_Lname, DOC_SSN, DOC_Email, DOC_Password, DOC_Specialisation, DOC_PhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = [
    ('3000', 'Ayman', 'Adel', '26409', 'ayman.adel@yahoo.com',
     '12345678900', 'Radiology', '01067841235'),
    ('3001', 'Ezzat', 'Mohamed', '27305', 'ezzat.mohamed@yahoo.com',
     '12345', 'Surgey', '01267841235'),
    ('3002', 'Essam', 'Adel', '26608', 'essam.adel@gmail.com',
     '78900', 'Medicine', '01167841235'),
    ('3003', 'Tamer', 'Ahmed', '2640', 'tamer.ahmed@icloud.com',
     '000000', 'Radiology', '01567841235'),
]
mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO Nurse (Nurse_ID, Nurse_Fname, Nurse_Lname, Nurse_SSN, Nurse_Email, Nurse_Password, Nurse_PhoneNo) VALUES (%s, %s, %s, %s,%s,%s,%s)"
val = [
    ('4000', 'Nadya', 'Nady', '2821',
     'nadia@gmail.com', '1123654850', '01587496301'),
    ('4001', 'Nagya', 'Nagy', '29001',
     'nagia3@gmail.com', 'nnnfd15', '01158996632'),
    ('4002', 'Fayza', 'Fayez', '2601',
     'fayzaf123@gmail.com', 'fa79846', '01026985111'),
    ('4003', 'Ne3mat', 'Mohamed', '1321564',
     'nn@gmail.com', '1234566543210', '01026222111'),
]

mycursor.executemany(sql, val)
mydb.commit()

##
sql = "INSERT INTO Patient (PAT_ID, PAT_Fname, PAT_Lname, PAT_SSN, PAT_Email, PAT_Password, PAT_RoomNo, PAT_PhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = [
    ('5000', 'Aly', 'Ibrahim', '2851',
     'aly@hotmail.com', 'aly1458693', '3201', '01008939915'),
    ('5001', 'Khaled', 'Aly', '28511',
     'khaled@yahoo.com', '265165165', '18205', '01206480119'),
    ('5002', 'Ahmed', 'Mossa', '25501',
     'ahmed@gmail.com', 'sacsa653135', '20503', '01062670067'),

]

mycursor.executemany(sql, val)
mydb.commit()


###
sql = "INSERT INTO Device (Device_ID, Device_Name) VALUES (%s, %s)"
val = [
    ('6000', 'MRI'),
    ('6001', 'CT'),
    ('6002', 'XRAY'),
    ('6003', 'Monitor'),
    ('6004', 'Ventilator'),
    ('6005', 'Infusion Pump'),
    ('6006', 'Syringe Pump'),
    ('6007', 'DC_Shock'),
]

mycursor.executemany(sql, val)
mydb.commit()


###
sql = "INSERT INTO Medications (Medication_ID, Medication_Name, Medication_Dose) VALUES (%s, %s, %s)"
val = [
    ('7000', 'dexamethasone ', 'three times'),
    ('7001', 'itobride', 'two times'),
    ('7002', 'paracetamol', 'one time'),
    ('7003', 'acetyle salsylate', 'five times'),
    ('7004', 'phenulepherine', 'four times'),
    ('7005', 'adrinaline', 'five times'),
    ('7006', 'dyphenhydramine', 'three times'),
    ('7007', 'doxylamine', 'two times'),
    ('7008', 'penicillin', 'one time'),
    ('7009', 'zofran', 'one time')
]

mycursor.executemany(sql, val)
mydb.commit()


sql = "INSERT INTO Maintenance (Device_Code, ENG_Code) VALUES (%s, %s)"
val = [
    ('6001', '2003'),
    ('6002', '2002'),
    ('6003', '2001'),
    ('6004', '2000'),
]

mycursor.executemany(sql, val)
mydb.commit()

###
sql = "INSERT INTO Cares (Nurse_Code, PAT_Code) VALUES (%s, %s)"
val = [
    ('4002', '5000'),
    ('4001', '5001'),
    ('4000', '5002'),

]

mycursor.executemany(sql, val)
mydb.commit()


###
sql = "INSERT INTO Checkup (DOC_Code, PAT_Code) VALUES (%s, %s)"
val = [
    ('3001', '5001'),
    ('3002', '5002'),
    ('3000', '5000'),
]

mycursor.executemany(sql, val)
mydb.commit()


###
sql = "INSERT INTO MedRelation (PAT_Code, DOC_Code, Medication_Code) VALUES (%s,%s,%s)"
val = [
    ('5001', '3001', '7001'),
    ('5000', '3000', '7002'),

]

mycursor.executemany(sql, val)
mydb.commit()

###
sql = "INSERT INTO Complain (Comp_No, PAT_Code, Comp_Msg) VALUES (%s, %s, %s)"
val = [
    ('1', '5001', 'Recovring well.'),
    ('2', '5002', 'Irregular heartbeat')
]

mycursor.executemany(sql, val)
mydb.commit()
