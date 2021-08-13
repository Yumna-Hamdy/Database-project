from flask import Flask, render_template, request
import mysql.connector
# from db_config import mysql
from flask import flash, render_template

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="icu"
)

mycursor = mydb.cursor()
app = Flask(__name__)


@app.route('/')
def home():
    data = ""
    global loginUser
    return render_template("home.html", data=loginUser)

# ------------------------ Signup ----------------------- #
@app.route('/addadmin', methods=['POST', 'GET'])
def addadmin():
    global userid
    id = userid
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":  # check if there is post data
        afname = request.form['afnme']
        alname = request.form['aLname']
        assn = request.form['assn']
        aid = request.form['aID']
        aemail = request.form['aemail']
        apassword = request.form['apsw']
        ano = request.form['atelephone']
        try:
            sql = "INSERT INTO Admin (Admin_Fname, Admin_Lname, Admin_SSN, Admin_ID, Admin_Email,  Admin_Password, Admin_PhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (afname, alname, assn, aid, aemail, apassword, ano)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('adminsignup.html')
        except:
            sql = "SELECT  Admin_Fname  FROM Admin  Where Admin_ID=%s "
            val = (aid,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult != None:
                return render_template('adminsignup.html', error="try another ID  ")
            else:
                return render_template('adminsignup.html', error="try another SSN ")
    else:
        return render_template('adminsignup.html')


@app.route('/addengineer', methods=['POST', 'GET'])
def addengineer():
    global userid
    id = userid
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":
        efname = request.form['efnme']
        elname = request.form['eLname']
        essn = request.form['essn']
        eid = request.form['eID']
        eemail = request.form['eemail']
        epassword = request.form['epsw']
        eno = request.form['etelephone']
        try:
            sql = "INSERT INTO Engineer (ENG_Fname, ENG_Lname, ENG_SSN, ENG_ID, ENG_Email,  ENG_Password,  ENG_PhoneNo) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
            val = (efname, elname, essn, eid, eemail, epassword, eno)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('engineersignup.html')
        except:
            sql = "SELECT  ENG_Fname  FROM Engineer  Where ENG_ID=%s "
            val = (eid,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult != None:
                return render_template('engineersignup.html', error="try another ID  ")
            else:
                return render_template('engineersignup.html', error="try another SSN ")

    else:
        return render_template('engineersignup.html')


@app.route('/addpatient', methods=['POST', 'GET'])
def addpatient():
    global userid
    id = userid
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":  # check if there is post data
        pfname = request.form['pfnme']
        plname = request.form['pLname']
        pssn = request.form['pssn']
        pid = request.form['pID']
        pemail = request.form['pemail']
        ppassword = request.form['ppsw']
        rno = request.form['roomnumber']
        pno = request.form['ptelephone']
        try:
            sql = "INSERT INTO Patient (PAT_Fname, PAT_Lname, PAT_SSN, PAT_ID, PAT_Email,  PAT_Password, PAT_RoomNo, PAT_PhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (pfname, plname, pssn, pid, pemail, ppassword, rno, pno)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('patientsignup.html')
        except:
            sql = "SELECT  PAT_Fname  FROM Patient  Where PAT_ID=%s "
            val = (pid,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult != None:
                return render_template('patientsignup.html', error="try another ID  ")
            else:
                return render_template('patientsignup.html', error="try another SSN ")

    else:
        return render_template('patientsignup.html')


@app.route('/adddoctor', methods=['POST', 'GET'])
def adddoctor():
    global userid
    id = userid
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":  # check if there is post data
        fname = request.form['fnme']
        lname = request.form['Lname']
        ssn = request.form['ssn']
        did = request.form['ID']
        email = request.form['email']
        password = request.form['psw']
        specialization = request.form['Specialization']
        no = request.form['telephone']
        try:

            sql = "INSERT INTO Doctor (DOC_Fname, DOC_Lname, DOC_SSN, DOC_ID, DOC_Email,  DOC_Password, DOC_Specialisation, DOC_PhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (fname, lname, ssn, did, email, password, specialization, no)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('doctorsignup.html')
        except:
            sql = "SELECT  DOC_Fname  FROM Doctor  Where DOC_ID=%s "
            val = (did,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult != None:
                return render_template('doctorsignup.html', error="try another ID  ")
            else:
                return render_template('doctorsignup.html', error="try another SSN ")

    else:
        return render_template('doctorsignup.html')


@app.route('/addnurse', methods=['POST', 'GET'])
def addnurse():
    global userid
    global loginUser
    id = userid
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":  # check if there is post data
        nfname = request.form['nfnme']
        nlname = request.form['nLname']
        nssn = request.form['nssn']
        nemail = request.form['nemail']
        nid = request.form['nID']
        npassword = request.form['npsw']
        nno = request.form['ntelephone']
        try:
            sql = "INSERT INTO Nurse (Nurse_Fname, Nurse_Lname, Nurse_SSN, Nurse_ID, Nurse_Email,  Nurse_Password, Nurse_PhoneNo) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
            val = (nfname, nlname, nssn, nid, nemail, npassword, nno)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('nursesignup.html')
        except:
            sql = "SELECT  Nurse_Fname  FROM Nurse  Where Nurse_ID=%s "
            val = (nid,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult != None:
                return render_template('nursesignup.html', error="try another ID  ")
            else:
                return render_template('nursesignup.html', error="try another SSN ")

    else:
        return render_template('nursesignup.html')
# ------------------------- End of Signup ------------------ #
# ---------------------add Medication ---------------------- #
@app.route('/addmedrelation', methods=['POST', 'GET'])
def addmedrelation():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "doctorProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        medid = request.form['mID']
        patientID = request.form['pid']
        docID = request.form['dID']

        SQLStatment = "INSERT INTO MedRelation ( PAT_Code, DOC_Code, Medication_Code) VALUES (%s, %s, %s)"
        val = (patientID, docID, medid)
        mycursor.execute(SQLStatment, val)
        mydb.commit()
        return render_template('successPage.html', Msg="Medication Added Successfully!")
    else:
        return render_template('addmedrelation.html', data=loginUser)


@app.route('/addmedication', methods=['POST', 'GET'])
def addmedication():
    global userid
    id = userid
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] == "engineerProfile" or loginUser[3] == "nurseProfile" or loginUser[3] == "patientProfile" or loginUser[3] == "" or loginUser[3] == None:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":
        medid = request.form['mID']
        medname = request.form['mname']
        meddoze = request.form['mdoze']

        mycursor.execute("SELECT * FROM Medications")
        myresult = mycursor.fetchall()
        for res in myresult:
            if (str(res[0]) == medid) or (str(res[1]) == medname):
                return render_template("failedPage.html", message1="This Relation already exists", message2="Please Enter a vaild Relation")

        SQLStatment = "INSERT INTO Medications ( Medication_ID, Medication_Name, Medication_Dose) VALUES (%s, %s, %s)"
        val = (medid, medname, meddoze)
        mycursor.execute(SQLStatment, val)
        mydb.commit()
        return render_template('doctorprofile.html', data=loginUser)
    else:
        return render_template('addmedication.html', data=loginUser)


# @app.route('/addmedication', methods=['POST', 'GET'])
# def addmedication():
#     global userid
#     id = userid
#     if request.method == "POST":
#         patid = request.form['pID']
#         medid = request.form['mID']
#         medname = request.form['mname']
#         meddoze = request.form['mdoze']
#         try:
#             aql = "SELECT  PAT_Fname  FROM Patient  Where PAT_ID=%s "
#             vall = (patid,)
#             mycursor.execute(aql, vall)
#             myresult = mycursor.fetchone()
#             print('myresult',myresult)
#             if myresult == None:
#                 return render_template('addmedication.html', error="check entered ID  ")

#             else:
#                 sql = "INSERT INTO Medications (Medication_ID, Medication_Name, Medication_Dose) VALUES (%s, %s, %s)"
#                 val = (medid, medname, meddoze)
#                 mycursor.execute(sql, val)
#                 mydb.commit()
#                 ssql = "INSERT INTO MedRelation (PAT_Code, Medication_Code, DOC_Code) VALUES (%s, %s, %s)"
#                 vval = (patid, medid, id)
#                 mycursor.execute(ssql, vval)
#                 mydb.commit()
#                 return render_template('addmedication.html')
#         except:
#             return render_template('addmedication.html', error="already exists  ")

#     else:
#         return render_template('addmedication.html')


# --------------------- End of add Medication ---------------------- #


# ------------------------ Login ---------------------- #
@app.route("/login/<string:prof>", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login(prof=1):
    if request.method == "POST":
        global userid
        global loginUser
        userid = request.form["lID"]
        userpassword = request.form["lpsw"]
        select = request.form.get('type')
        if select == "doctor":
            sql = "SELECT  DOC_Fname, DOC_Password, DOC_ID  FROM Doctor  Where DOC_ID=%s "
            val = (userid,)
            mycursor.execute(sql, val)
            loginUser = mycursor.fetchone()
            prof = "doctorProfile"
            if loginUser == None:
                return render_template("failedPage.html", message1="Wrong ID or Password", message2="Please Try agian.")

            loginUser = loginUser + (prof,)
            if loginUser[1] == userpassword:
                return render_template('home.html', data=loginUser)
            else:
                return render_template('alert.html')
        elif select == "nurse":
            sql = "SELECT  Nurse_Fname, Nurse_Password, Nurse_ID  FROM Nurse  Where Nurse_ID=%s "
            val = (userid,)
            mycursor.execute(sql, val)
            loginUser = mycursor.fetchone()
            if loginUser == None:
                return render_template("failedPage.html", message1="Wrong ID or Password", message2="Please Try agian.")
            prof = "nurseProfile"
            loginUser = loginUser + (prof,)
            if loginUser[1] == userpassword:
                return render_template('home.html', data=loginUser)
            else:
                return render_template('alert.html')

        elif select == "patient":
            sql = "SELECT  PAT_Fname, PAT_Password, PAT_ID  FROM Patient  Where PAT_ID=%s "
            val = (userid,)
            mycursor.execute(sql, val)
            loginUser = mycursor.fetchone()
            prof = "patientProfile"
            if loginUser == None:
                return render_template("failedPage.html", message1="Wrong ID or Password", message2="Please Try agian.")
            loginUser = loginUser + (prof,)
            if loginUser[1] == userpassword:
                return render_template('home.html', data=loginUser)
            else:
                return render_template('alert.html')

        elif select == "engineer":
            sql = "SELECT  ENG_Fname, ENG_Password, ENG_ID  FROM Engineer  Where ENG_ID=%s "
            val = (userid,)
            mycursor.execute(sql, val)
            loginUser = mycursor.fetchone()
            prof = "engineerProfile"
            if loginUser == None:
                return render_template("failedPage.html", message1="Wrong ID or Password", message2="Please Try agian.")
            loginUser = loginUser + (prof,)
            if loginUser[1] == userpassword:
                return render_template('home.html', data=loginUser)
            else:
                return render_template('alert.html')

        elif select == "admin":
            sql = "SELECT  Admin_Fname, Admin_Password, Admin_ID  FROM Admin Where Admin_ID=%s "
            val = (userid,)
            mycursor.execute(sql, val)
            loginUser = mycursor.fetchone()
            prof = "adminProfile"
            if loginUser == None:
                return render_template("failedPage.html", message1="Wrong ID or Password", message2="Please Try agian.")
            loginUser = loginUser + (prof,)
            if loginUser[1] == userpassword:
                return render_template('home.html', data=loginUser)
            else:
                return render_template('alert.html')
    else:
        return render_template('loginuser.html')
# ------------------------ End of Login ----------------- #


# ----------------------- Devices ---------------------- #
@app.route('/devicePortal')
def devicePortal():
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    return render_template("devicePortal.html")


@app.route('/adddevice', methods=['GET', 'POST'])
def addDevice():
    global userid
    id = userid
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        dev_name = request.form["device_name"]
        dev_id = request.form["device_id"]

        mycursor.execute("SELECT * FROM Device")
        myresult = mycursor.fetchall()
        for res in myresult:
            if str(res[0]) == dev_id and str(res[1]) == dev_name:
                return render_template("failedPage.html", message1="This Device already exists", message2="Please Enter another device")

        val = (dev_name, dev_id)
        Q = "INSERT INTO Device (Device_Name , Device_ID) VALUES (%s,%s)"
        mycursor.execute(Q, val)
        mydb.commit()
        return render_template("devicePortal.html")
    else:
        return render_template("addDevice.html")


@app.route('/viewdeviceTable')
def viewDevicesTable():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    Q = "SELECT * FROM Device"
    mycursor.execute(Q)

    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }

    return render_template("viewDevicesTable.html", data=data)


@app.route('/viewDevice')
def viewDevice():
    Q = "SELECT * FROM Device"
    mycursor.execute(Q)
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    deviceData = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template("viewDevice.html", devicedata=deviceData)

# ----------------------- End of Devices ---------------------- #


# ----------------------- Engineer ---------------------- #
@app.route('/engineerPortal', methods=['GET', 'POST'])
def engineerPortal():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        ENG_id = request.form['engID']
        mycursor.execute(
            "SELECT Device_ID, Device_Name FROM Engineer JOIN Maintenance ON ENG_ID = ENG_Code JOIN Device ON Device_ID = Device_Code  WHERE ENG_Code =  %s", (ENG_id,))
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        print(data['rec'])

        mycursor.execute(
            "SELECT ENG_Fname, ENG_Lname FROM Engineer WHERE ENG_ID = %s", (ENG_id,))
        engResult = mycursor.fetchone()
        return render_template('viewEngToDev.html', data=data, doc=engResult)
    else:
        return render_template('engineerPortal.html')


@app.route('/engtodev', methods=['GET', 'POST'])
def engtodev():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        eng_id = request.form["engineer_id"]
        dev_id = request.form["device_id"]
        mycursor.execute("SELECT * FROM Maintenance")
        myresult = mycursor.fetchall()
        for res in myresult:
            if str(res[0]) == dev_id and str(res[1]) == eng_id:
                return render_template("failedPage.html", message1="This Relation already exists", message2="Please Enter a vaild Relation")

        val = (dev_id, eng_id)
        Q = "INSERT INTO Maintenance (Device_Code , ENG_Code) VALUES (%s,%s)"
        mycursor.execute(Q, val)
        mydb.commit()

        mycursor.execute("SELECT * FROM Maintenance")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult2 = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'rec': myresult2,
            'header': row_headers
        }

        return render_template('viewMaintenance.html', data=data)
    else:
        return render_template("addEngToDevice.html")

    ################### Added ################


@app.route('/viewengineer')
def viewengineer():
    Q = "SELECT * FROM engineer"
    mycursor.execute(Q)
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    engineers = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template("viewengineer.html", engineers_data=engineers)


@app.route('/viewengineerTable')
def viewengineerTable():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    Q = "SELECT * FROM engineer"
    mycursor.execute(Q)
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    engineers2 = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template("viewEngineerTable.html", data=engineers2)


@app.route('/viewengtodev')
def viewengtodev():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    Q = "SELECT * FROM Maintenance"
    mycursor.execute(Q)
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    deviceData = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }

    return render_template("viewEngToDev.html", maint_data=myresult)


@app.route('/pickeng', methods=['GET', 'POST'])
def pickeng():
    if request.method == 'POST':
        Engg_id = request.form['engg_idd']
        mycursor.execute(
            "SELECT Device_ID , Device_Name FROM Engineer JOIN Maintenance ON ENG_ID = ENG_Code JOIN Device ON Device_ID = Device_Code  WHERE ENG_Code =  %s", (Engg_id,))
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()

        careData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('pickEng.html', dataa=myresult)
    else:
        return render_template('pickEng.html')


@app.route('/viewMaintenance')
def viewMaintenance():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Maintenance")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewMaintenance.html', data=data)

# ----------------------- End of Engineer ---------------------- #

#------------------------- Start Upload Scan --------------------------#


@app.route('/uploadScan', methods=['GET', 'POST'])
def uploadScan():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "doctorProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        filePath = request.form['myfile']
        patientID = request.form['patid']
        docID = request.form['docID']
        docName = request.form['docName']
        scanDescritpion = request.form['scanDescritpion']
        with open(filePath, "rb") as File:
            BinaryData = File.read()
        SQLStatment = "INSERT INTO images (Photo, PAT_Code, DOC_Code, DOC_Name, Scan_Description) VALUES (%s, %s, %s, %s, %s)"
        val = (BinaryData, patientID, docID, docName, scanDescritpion)
        mycursor.execute(SQLStatment, val)
        mydb.commit()
        return render_template('successPage.html', Msg="Scan Added to Patient Successfully!")
    else:
        return render_template('uploadScan.html', data=loginUser)


@app.route('/showScan', methods=['GET', 'POST'])
def showScan():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "patientProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    global userid
    id = userid
    sql = "SELECT * FROM  Images WHERE PAT_Code = %s"
    value = (id,)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchall()
    c = ""
    imgPaths = []
    for i in range(len(myresult)):
        ImagePath = "static/images/img{0}.jpg".format(str(id+str(c)))
        imgPaths.append(ImagePath)
        c = c + "19999"

    for i in range(len(imgPaths)):
        with open(imgPaths[i], "wb") as File:
            for index, res in enumerate(myresult[i]):
                if index == 1:
                    File.write(res)
                else:
                    pass
        File.close()

    sql2 = "SELECT DOC_Code, DOC_Name, Scan_Description FROM Images WHERE PAT_Code = %s"
    value2 = (id,)
    mycursor.execute(sql2, value2)
    result = mycursor.fetchall()
    # data = data['rec'][2]
    allData = []
    for index, value in enumerate(result):
        value = value + (imgPaths[index],)
        allData.append(value)
    return render_template('showScan.html', data=allData)
    # return "ai haga"

#------------------------- End Upload Scan --------------------------#


# ----------------------- Contact Us ---------------------- #
@app.route('/contactus', methods=['GET', 'POST'])
def contact():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "patientProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        cNo = 3
        pat_code = request.form["pat_code"]
        msg = request.form["message"]
        sql = "INSERT INTO Complain (Comp_No, PAT_Code, Comp_Msg) VALUES (%s, %s, %s)"
        val = (cNo, pat_code, msg)
        mycursor.execute(sql, val)
        mydb.commit()
        data = ""
        return render_template("home.html")
    else:
        data = ""
        return render_template("contact.html", data=loginUser)
# ----------------------- End of Contact Us ---------------------- #


# ---------------------------  PATIENT ---------------------- #
@app.route('/patientPortal')
def patientPortalPage():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    return render_template("patientPortal.html")


@app.route('/viewPatientTable')
def viewPatientTable():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Patient")
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        patientData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewPatientTable.html', data=patientData)


@app.route('/viewPatient')
def viewPatient():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Patient")
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        patientData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewPatient.html', data=patientData)
# ---------------------------  End of  PATIENT ---------------------- #


# ---------------------------  Nurse to PATIENT ---------------------- #
@app.route('/addCare', methods=['GET', 'POST'])
def addCare():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":
        Nurse_Id = request.form['nurseID']
        PAT_Id = request.form['patientID']
        mycursor.execute("SELECT * FROM Cares")
        myresult = mycursor.fetchall()
        for res in myresult:
            if str(res[0]) == Nurse_Id and str(res[1]) == PAT_Id:
                return render_template("failedPage.html", message1="This Relation already exists", message2="Please Enter a vaild Relation")

        sql = '''INSERT INTO Cares (Nurse_Code, PAT_Code)
                 VALUES (%s, %s)'''
        val = (Nurse_Id, PAT_Id)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("SELECT * FROM Cares")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult2 = mycursor.fetchall()
        careDataRetrieved = {
            'message': "data retrieved",
            'rec': myresult2,
            'header': row_headers
        }
        return render_template("viewCares.html", data=careDataRetrieved)
    return render_template("addNurseToPatient.html")


@app.route('/viewCare')
def viewCare():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Cares")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        careData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewCares.html', data=careData)
# ------------------------  End of Nurse to PATIENT -------------------- #


# --------------------------- Nurse ---------------------- #
@app.route('/nursePortal', methods=['GET', 'POST'])
def nursePortal():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        N_id = request.form['nurseID']
        mycursor.execute(
            "SELECT PAT_Fname, PAT_Lname, PAT_SSN, PAT_ID, PAT_Email, PAT_Password, PAT_RoomNo, PAT_PhoneNo FROM Nurse JOIN Cares ON Nurse_ID = Nurse_Code JOIN Patient ON PAT_ID = PAT_Code  WHERE Nurse_Code =  %s", (N_id,))
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        careData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }

        mycursor.execute(
            "SELECT Nurse_Fname, Nurse_Lname FROM Nurse WHERE Nurse_ID = %s", (N_id,))
        nurseResult = mycursor.fetchone()

        return render_template('viewPatientRelatesToNurse.html', data=careData, nurse=nurseResult)
    else:
        return render_template('nursePortal.html')


@app.route('/viewNurseTable')
def viewNurseTable():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Nurse")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        nurseData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewNurseTable.html', data=nurseData)


@app.route('/viewNurse')
def viewNurse():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Nurse")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        nurseData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewNurse.html', data=nurseData)
# ---------------------------  End of Nurse ---------------------- #


# -------------------------- Statistics ---------------------- #
@app.route('/statistics', methods=['POST', 'GET'])
def statistics():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "GET":
        doctorCount = 0
        patientCount = 0
        nurseCount = 0
        engineerCount = 0
        deviceCount = 0

        mycursor.execute("SELECT COUNT(DOC_ID) FROM Doctor")
        result1 = mycursor.fetchall()
        doctorCount = (result1[0])[0]

        mycursor.execute("SELECT COUNT(PAT_ID) FROM Patient")
        result2 = mycursor.fetchall()
        patientCount = (result2[0])[0]

        mycursor.execute("SELECT COUNT(Nurse_ID) FROM Nurse")
        result3 = mycursor.fetchall()
        nurseCount = (result3[0])[0]

        mycursor.execute("SELECT COUNT(ENG_ID) FROM Engineer")
        result4 = mycursor.fetchall()
        engineerCount = (result4[0])[0]

        mycursor.execute("SELECT COUNT(Device_ID) FROM Device")
        result5 = mycursor.fetchall()
        deviceCount = (result5[0])[0]

        totalPeople = doctorCount + patientCount + engineerCount + nurseCount
        mem = [doctorCount, nurseCount, engineerCount, patientCount]
        label = ["No. Of Doctors", "No. of Nurses",
                 "No. of Engineers", "No. of Patients"]

        labels = [
            'No. Of Doctors', 'No. of Nurses', 'No. of Engineers', 'No. of Patients',
        ]

        values = [
            doctorCount, nurseCount, engineerCount, patientCount,
        ]

        colors = [
            "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
            "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

        pie_labels = labels
        pie_values = values
        return render_template("statistics.html", chartd=mem, labels=label,  max=17000, set=zip(values, labels, colors))
    else:
        return render_template("statistics.html")
    # ------------------------- End of Statistics ---------------- #

# ---------------------- Doctors -------------------- #
@app.route('/doctorPortal', methods=['GET', 'POST'])
def doctorPortal():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        DOC_Id = request.form['doctorID']
        mycursor.execute(
            "SELECT PAT_Fname, PAT_Lname, PAT_SSN, PAT_ID, PAT_Email, PAT_RoomNo, PAT_PhoneNo FROM Doctor JOIN Checkup ON DOC_ID = DOC_Code JOIN Patient ON PAT_ID = PAT_Code  WHERE DOC_Code =  %s", (DOC_Id,))
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        checkUp = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }

        mycursor.execute(
            "SELECT DOC_Fname, DOC_Lname FROM Doctor WHERE DOC_ID = %s", (DOC_Id,))
        docResult = mycursor.fetchone()

        return render_template('viewPatientRelatesToDoctor.html', data=checkUp, doc=docResult)
    else:
        return render_template('doctorPortal.html')


@app.route('/viewDoctorsTable')
def viewDoctorTable():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Doctor")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        doctoreData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewDoctorsTable.html', data=doctoreData)


@app.route('/viewDoctor')
def viewDoctor():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Doctor")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        doctorData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewDoctor.html', data=doctorData)

# ---------------------- End of Doctors -------------------- #
# ---------------------- Start of Doctors/Patient -------------------- #


@app.route('/addCheckUp', methods=['GET', 'POST'])
def addCheckUP():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":
        Doctor_Id = request.form['doctorID']
        PAT_Id = request.form['patientID']
        mycursor.execute("SELECT * FROM checkup")
        myresult = mycursor.fetchall()
        for res in myresult:
            if str(res[0]) == Doctor_Id and str(res[1]) == PAT_Id:
                return render_template("failedPage.html", message1="This Relation already exists", message2="Please Enter a vaild Relation")

        sql = '''INSERT INTO Checkup (DOC_Code, PAT_Code)
                 VALUES (%s, %s)'''
        val = (Doctor_Id, PAT_Id)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("SELECT * FROM checkup")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult2 = mycursor.fetchall()
        checkUpDataRetrieved = {
            'message': "data retrieved",
            'rec': myresult2,
            'header': row_headers
        }
        return render_template("viewCheckUps.html", data=checkUpDataRetrieved)
    return render_template("addDoctorToPatient.html")


@app.route('/viewCheckUps')
def viewCheckUps():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM checkup")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        checkupData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewCheckUps.html', data=checkupData)
# ---------------------- End of Doctors/Patient -------------------- #


# --------------------- Doctors Profile ---------------------- #
@app.route('/doctorProfile')
def doctorProfile():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "doctorProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    global userid
    id = userid
    sql = "SELECT * FROM Doctor WHERE DOC_ID = %s"
    value = (id,)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchone()
    return render_template('doctorProfile.html', data=myresult)

# --------------------- End of Doctors Profile ---------------------- #


# --------------------- Engineer Profile ---------------------- #
# @app.route('/engineerProfile', methods=["POST", "GET"])
# def engineerProfile():
#     if request.method == "POST":
#         return render_template("engineerProfile.html")
#     else:
#         return render_template("engineerProfile.html")

@app.route('/engineerProfile')
def engineerProfile():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "engineerProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    global userid
    id = userid
    sql = "SELECT * FROM Engineer WHERE ENG_ID = %s"
    value = (id,)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchone()
    return render_template('engineerProfile.html', data=myresult)

# --------------------- End of Engineer Profile ---------------------- #


# --------------------- Nurse Profile ---------------------- #
# @app.route('/nurseProfile', methods=["POST", "GET"])
# def nurseProfile():
#     if request.method == "POST":
#         return render_template("nurseProfile.html")
#     else:
#         return render_template("nurseProfile.html")

@app.route('/nurseProfile')
def nurseProfile():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "nurseProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    global userid
    id = userid
    sql = "SELECT * FROM Nurse WHERE Nurse_ID = %s"
    value = (id,)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchone()
    return render_template('nurseProfile.html', data=myresult)

# --------------------- End of Nurse Profile ---------------------- #


# --------------------- Patient Profile ---------------------- #
@app.route('/patientProfile')
def patientProfile():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "patientProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    global userid
    id = userid
    sql = "SELECT * FROM Patient WHERE PAT_ID = %s"
    value = (id,)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchone()
    return render_template('patientProfile.html', data=myresult)

# --------------------- End of Patient Profile ---------------------- #


# --------------------- Admin Profile ---------------------- #
# @app.route('/adminProfile', methods=["POST", "GET"])
# def adminProfile():
#     if request.method == "POST":
#         return render_template("adminProfile.html")
#     else:
#         return render_template("adminProfile.html")

@app.route('/adminProfile')
def adminProfile():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    global userid
    id = userid
    sql = "SELECT * FROM admin WHERE Admin_ID = %s"
    value = (id,)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchone()
    return render_template('adminProfile.html', data=myresult)

# --------------------- End of Admin Profile ---------------------- #
# ---------------------view Medication ---------------------- #
@app.route('/viewmedication')
def viewmwdication():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "patientProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    global userid
    id = userid
    sql = "SELECT Medication_ID, Medication_Name, Medication_Dose  FROM  Medications   JOIN MedRelation ON Medication_ID = Medication_Code JOIN Patient ON PAT_Code = PAT_ID WHERE PAT_ID = %s"
    value = (id,)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchall()
    return render_template('viewmedication.html', med=myresult)
# --------------------- end view Medication ---------------------- #
#------------------------ View Medication table ------------------------#
@app.route('/viewMedicationTable')
def viewMedicationTable():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM Medications")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        medsData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewMedicationTable.html', data=medsData)
#------------------------ end of View Medication table ------------------------#
#------------------------ Medication portal ------------------------#
@app.route('/medicationPortal')
def medicationPortal():
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    return render_template("medicationPortal.html")
#------------------------ end of Medication portal ------------------------#
#------------------------ Medication partient relation ------------------------#


@app.route('/viewmedstopats')
def viewmedstopats():
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == 'POST':
        return render_template('home.html')
    else:
        mycursor.execute("SELECT * FROM MedRelation")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        medstopats = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewMedicationsToPatient.html', data=medstopats)
#------------------------ end of Medication partient relation ------------------------#

#------------------------ Medication signup ------------------------#


@app.route('/medicationsSignup', methods=['POST', 'GET'])
def medicationsSignup():
    global userid
    id = userid
    global loginUser
    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] == "engineerProfile" or loginUser[3] == "nurseProfile" or loginUser[3] == "patientProfile" or loginUser[3] == "" or loginUser[3] == None:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":
        medid = request.form['mID']
        medname = request.form['mname']
        meddoze = request.form['mdoze']

        mycursor.execute("SELECT * FROM Medications")
        myresult = mycursor.fetchall()
        for res in myresult:
            if (str(res[0]) == medid) or (str(res[1]) == medname):
                return render_template("failedPage.html", message1="This Relation already exists", message2="Please Enter a vaild Relation")

        SQLStatment = "INSERT INTO Medications ( Medication_ID, Medication_Name, Medication_Dose) VALUES (%s, %s, %s)"
        val = (medid, medname, meddoze)
        mycursor.execute(SQLStatment, val)
        mydb.commit()
        return render_template('home.html', data=loginUser)
    else:
        return render_template('medicationsSignup.html', data=loginUser)

# --------------------- Drop Data ---------------------- #
@app.route('/dropData', methods=['GET', 'POST'])
def dropData():
    global loginUser

    if len(loginUser) == 0:
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if loginUser[3] != "adminProfile":
        return render_template("failedPage.html", message1="Either you aren't cool enough to visit this page or it doesn't exist", message2="like your social life.")

    if request.method == "POST":
        global userid
        userid = request.form["userID"]
        select = request.form.get('type')
        if select == "doctor":
            val = (userid,)
            sql = "SELECT * FROM Doctor WHERE DOC_ID=%s"
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult == None:
                return render_template("failedPage.html", message1="Doctor's ID doesn't exist", message2="try again.")

            sql1 = "DELETE FROM CheckUp WHERE DOC_Code=%s"
            mycursor.execute(sql1, val)
            mydb.commit()

            sql2 = "DELETE FROM Doctor Where DOC_ID=%s "
            mycursor.execute(sql2, val)
            mydb.commit()
            return render_template('successPage.html', Msg="Doctor Delete Sucessfully")

        if select == "nurse":
            val = (userid,)
            sql = "SELECT * FROM Nurse WHERE Nurse_ID=%s"
            val = (userid,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult == None:
                return render_template("failedPage.html", message1="Nurse's ID doesn't exist", message2="try again.")

            sql1 = "DELETE FROM Cares WHERE Nurse_Code=%s"
            mycursor.execute(sql1, val)
            mydb.commit()

            sql2 = "DELETE FROM Nurse Where Nurse_ID=%s "
            mycursor.execute(sql2, val)
            mydb.commit()
            return render_template('successPage.html', Msg="Nurse Delete Sucessfully")

        if select == "patient":
            val = (userid,)
            sql = "SELECT * FROM Patient WHERE PAT_ID=%s"
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult == None:
                return render_template("failedPage.html", message1="Patient's ID doesn't exist", message2="try again.")

            sql1 = "DELETE FROM CheckUp WHERE PAT_Code=%s"
            mycursor.execute(sql1, val)
            mydb.commit()

            sql2 = "DELETE FROM Cares WHERE PAT_Code=%s"
            mycursor.execute(sql2, val)
            mydb.commit()

            sql3 = "DELETE FROM Images WHERE PAT_Code=%s "
            mycursor.execute(sql3, val)
            mydb.commit()

            sql4 = "DELETE FROM MedRelation WHERE PAT_Code=%s "
            mycursor.execute(sql4, val)
            mydb.commit()

            sql5 = "DELETE FROM Complain WHERE PAT_Code=%s "
            mycursor.execute(sql5, val)
            mydb.commit()

            sql6 = "DELETE FROM Patient WHERE PAT_ID=%s "
            mycursor.execute(sql6, val)
            mydb.commit()
            return render_template('successPage.html', Msg="Patient Delete Sucessfully")

        if select == "engineer":
            val = (userid,)
            sql = "SELECT * FROM Engineer WHERE ENG_ID=%s"
            val = (userid,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult == None:
                return render_template("failedPage.html", message1="Engineer's ID doesn't exist", message2="try again.")

            sql1 = "DELETE FROM Maintenance WHERE ENG_Code=%s"
            mycursor.execute(sql1, val)
            mydb.commit()

            sql2 = "DELETE FROM Engineer WHERE ENG_ID=%s "
            mycursor.execute(sql2, val)
            mydb.commit()
            return render_template('successPage.html', Msg="Engineer Delete Sucessfully")

        if select == "device":
            val = (userid,)
            sql = "SELECT * FROM Device WHERE Device_ID=%s"
            val = (userid,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult == None:
                return render_template("failedPage.html", message1="Device's ID doesn't exist", message2="try again.")

            sql1 = "DELETE FROM Maintenance WHERE Device_Code=%s"
            mycursor.execute(sql1, val)
            mydb.commit()

            sql2 = "DELETE FROM Device WHERE Device_ID=%s "
            mycursor.execute(sql2, val)
            mydb.commit()
            return render_template('successPage.html', Msg="Device Delete Sucessfully")

        if select == "medication":
            val = (userid,)
            sql = "SELECT * FROM Medications WHERE DOC_ID=%s"
            val = (userid,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult == None:
                return render_template("failedPage.html", message1="Medication's ID doesn't exist", message2="try again.")

            sql1 = "DELETE FROM MedRelation WHERE Medication_Code=%s"
            mycursor.execute(sql1, val)
            mydb.commit()

            sql2 = "DELETE FROM Medications WHERE Medication_ID=%s "
            mycursor.execute(sql2, val)
            mydb.commit()
            return render_template('successPage.html', Msg="Medication Delete Sucessfully")

        if select == "admin":
            val = (userid,)
            if str(userid) == "1":
                return render_template("failedPage.html", message1="You Can't Delete the main Admin", message2="no racism")

            sql = "SELECT * FROM Admin WHERE Admin_ID=%s"
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            if myresult == None:
                return render_template("failedPage.html", message1="Admin's ID doesn't exist", message2="try again.")

            sql1 = "DELETE FROM Admin WHERE Admin_ID=%s"
            mycursor.execute(sql1, val)
            mydb.commit()

            return render_template('successPage.html', Msg="Admin Delete Sucessfully")

    else:
        return render_template('dropData.html')
    # return render_template('dropData.html')
# --------------------- End of Drop Data ---------------------- #


if __name__ == '__main__':
    userid = ''
    loginUser = ''
    app.run()
