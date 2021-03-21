#! /usr/bin/python3.9

####################################
#   RIFARE CON I DATABASE NO CSV   #
####################################

#from main import disegno, scelta
from main import *

import csv
import getpass
import hashlib
import subprocess
from password_strength import PasswordPolicy

global data
data = {"id": "",
        "username": "",
        "password": "",
        "email": "",
        "block": "",
        "firstTime": ""}


def passwordStrength(password):
    from password_strength import PasswordStats
    stats = PasswordStats(password)
    strength = round(stats.strength(), 3)
    x = "Password strength [{}/0.999] -> ".format(strength)
    if 0.0 <= strength and strength <= 0.333:
        x += "[weak]"
    elif 0.334 <= strength and strength <= 0.666:
        x += "[medium]"
    else:
        x += "[strong]"
    print(x)


def sendMail(email, opzione):
    from email.message import EmailMessage
    # Opzione
    # 0) mail register()
    # 1) mail forgotPassword()
    # 2) mail changePassword()
    import smtplib
    import random

    emailTool = ""  # YOUR EMAIL
    passwordTool = ""  # https://myaccount.google.com/apppasswords

    code = ""
    for i in range(5):
        code += chr(random.randint(33, 126))
    if opzione == 0:
        subject = "Register verification code"
        body = "Your register verification code is:"
    elif opzione == 1:
        subject = "Forgot password verification code"
        body = "Your forgot password verification code is:"
    else:
        subject = "Change password verification code"
        body = "Your change password verification code is:"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = emailTool
    msg['To'] = email
    msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <head>
            <style>
                body{
                    margin: 0;
                    padding: 0;
                }
    
                #container{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    width: 450px;
                    height: 600px;
                    font-size: larger;
                    color:black;
                    background-color: rgb(71, 71, 71);
                    font-family: Verdana, Geneva, Tahoma, sans-serif;
                }
    
                #titolo{
                    font-size: 100px;
                    color: green;
                    padding-bottom: 50px;
                }
    
                #msg{
                    display: flex;
                    margin-top: 50px;
                    flex-direction: column;
                    align-items: center;
                }
    
                #code{
                    font-size: 100px;
                }
            </style>
            </head>
            <body>
            <div id="container">
                <div id="titolo">HackTool</div>
                <div id="msg">
                    <div id="corpo">""" + body + """</div>
                    <div id="code">""" + code + """</div>
                </div>
            </div>
            </body>
        </html>
    """, subtype='html')



    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(emailTool, passwordTool)  # Login in gmail

        # esito 0 -> tutto ok
        # esito 1 -> mail sbagliata
        # esito 2 -> codice errato

        esito = 0
        try:
            smtp.send_message(msg)
        except:
            esito = 1
            return esito

        verifyCode = input("Insert the code we sent you via email: ")

        if code == verifyCode:
            return esito
        else:
            esito = 2
            return esito


def updateCSV():
    reader = csv.reader(open("userDB.csv"), delimiter='|')
    lines = list(reader)
    # print(lines)
    for i in range(len(lines)):
        # print(lines[i][1])
        if lines[i][1] == data["username"]:
            lines[i][2] = data["password"]
            lines[i][3] = data["email"]
            lines[i][4] = data["block"]
            lines[i][5] = data["firstTime"]
            writer = csv.writer(open('userDB.csv', 'w'), delimiter='|')
            writer.writerows(lines)
            #########################################
            #    DA ERRORE OGNITANTO MA FUNZIONA    #
            #########################################
    # print("Update settings successful!")


def loginRegisterMenu():
    disegno()
    print("|                 HELLO USER                    |")
    print("+-----------------------------------------------+")
    print("1) Login\n2) Register\n")
    x = scelta(1, 2)
    if x == 1:
        login()
    else:
        register()


def login():
    disegno()
    print("|                 LOGIN MENU                    |")
    print("+-----------------------------------------------+")
    print("1) Login\n2) Forgot password\n")
    x = scelta(1, 2)
    if x == 1:
        disegno()
        print("|                   LOGIN                       |")
        print("+-----------------------------------------------+")

        error = 0
        while True:
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            passwordHash = hashlib.sha256(password.encode('utf-8')).hexdigest()  # hashing della password

            # Leggo CSV [userDB.csv]
            with open('userDB.csv', newline='\n') as csvfile:
                reader = csv.DictReader(csvfile, delimiter='|')
                for row in reader:
                    # Trovo la riga col nome e lavoro su quella
                    if row["username"] == username and row["password"] == passwordHash:
                        data["id"] = row["id"]
                        data["username"] = row["username"]
                        data["password"] = row["password"]
                        data["email"] = row["email"]
                        data["block"] = row["block"]
                        data["firstTime"] = row["firstTime"]
                        if data["firstTime"] == "1":
                            settings()
                            exit()
                        else:
                            mainMenu()
                            exit()
                print("Invalid credential...\n")
                error += 1
                if error == 3:
                    print("Sorry we must block you!")
                    exit()
    else:
        forgotPassword()


def forgotPassword():
    disegno()
    print("|               FORGOT PASSWORD                 |")
    print("+-----------------------------------------------+")
    while True:
        username = input("Username: ")
        email = input("Email: ")
        controllo = 0
        if "." in email and "@" in email:
            reader = csv.reader(open("userDB.csv"), delimiter='|')
            lines = list(reader)
            for i in range(len(lines)):
                if lines[i][1] == username and lines[i][3] == email:
                    controllo = 1
                    # Criteri della password
                    policy = PasswordPolicy.from_names(
                        length=8,  # min length: 8
                        uppercase=1,  # need min. 1 uppercase letters
                        numbers=1,  # need min. 1 digits
                        special=1,  # need min. 1 special characters
                        nonletters=1,  # need min. 1 non-letter characters (digits, specials, anything)
                    )
                    while True:
                        password1 = getpass.getpass(
                            "Password must contain:\n- 8 Character\n- Number\n- Uppercase character\n- Special character\nPassword: ")
                        if len(policy.test(password1)) == 0:
                            # Password strength
                            passwordStrength(password1)
                            password2 = getpass.getpass("Confirm password: ")
                            if password1 == password2:
                                esito = sendMail(email, 1)
                                if esito == 0:
                                    passwordHash = hashlib.sha256(password1.encode('utf-8')).hexdigest()
                                    lines[i][2] = passwordHash
                                    writer = csv.writer(open('userDB.csv', 'w'), delimiter='|')
                                    writer.writerows(lines)
                                    break
                                elif esito == 1:
                                    print("Invalid email!")
                                else:
                                    print("Invalid code!")
                            else:
                                print("Password doesn't match!")
                        print("")
            if controllo == 1:
                print("Password was change successful!\n")
                x = input("Press any key to go to login menu ")
                login()
            else:
                print("Invalid credential...\n")
        else:
            print("Invalid email!\n")


def register():
    disegno()
    print("|                  REGISTER                     |")
    print("+-----------------------------------------------+")

    # Scorro database dei nomi per vedere se il nome è gia registrato
    # Primary key [id]
    # Foreign key [username]

    # ---Soluzione intelligente per database grandi-------------------------------
    # Controllo se l username non è presente
    userDB = []
    id = 0
    with open('userDB.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            # Carico l'intero database colonna username in una lista
            userDB.append(row["username"])
            id += 1

    while True:
        username: str = input("Username: ")
        # Scorro la lista per vedere se il nome è gia usato in tal caso errore
        if username in userDB:
            print("Username already used!\n")
        else:
            break

    # ---Soluzione intelligente per database piccoli--------------------------------
    # Funzional ma non troppo in quanto se nella password cifrata si presenta
    # lo username il programma dirà che il nome gia esiste

    # username = input('Enter username >')
    # if username in open('names.csv', 'r').read():
    #    print('Username already exists')
    # -----------------------------------------------------------------------------

    # Criteri della password
    policy = PasswordPolicy.from_names(
        length=8,  # min length: 8
        uppercase=1,  # need min. 1 uppercase letters
        numbers=1,  # need min. 1 digits
        special=1,  # need min. 1 special characters
        nonletters=1,  # need min. 1 non-letter characters (digits, specials, anything)
    )
    while True:
        password1 = getpass.getpass(
            "Password must contain:\n- 8 Character\n- Number\n- Uppercase character\n- Special character\nPassword: ")
        if len(policy.test(password1)) == 0:
            # Password strength
            passwordStrength(password1)
            password2 = getpass.getpass("Confirm password: ")
            if password1 == password2:
                passwordHash = hashlib.sha256(password1.encode('utf-8')).hexdigest()

                while True:
                    # Controllo formale email
                    while True:
                        email = input("Email: ")
                        if "." in email and "@" in email:
                            esito = sendMail(email, 0)
                            if esito == 0:
                                wfile = open("userDB.csv", "a")
                                wfile.write(str(id) + "|" + username + "|" + passwordHash + "|" + email + "|0|1\n")
                                wfile.close()

                                login()
                            elif esito == 1:
                                print("Invalid email!\n")
                            else:
                                print("Invalid code!\n")
                        else:
                            print("Invalid email!\n")
            else:
                print("Password doesn't match!\n")
        else:
            print("")


def settings():
    # Impostazioni dell account (API/shortcut)
    disegno()
    print("|                  SETTINGS                     |")
    print("+-----------------------------------------------+")
    data["firstTime"] = "0"
    updateCSV()
    print("1) Change password\n2) Back to menu\n")
    x = scelta(1, 2)
    if x == 1:
        changePassword()
    else:
        mainMenu()


def changePassword():
    disegno()
    print("|               CHANGE PASSWORD                 |")
    print("+-----------------------------------------------+")

    while True:
        password = getpass.getpass("Password: ")
        passwordHash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        controllo = 0
        reader = csv.reader(open("userDB.csv"), delimiter='|')
        lines = list(reader)
        for i in range(len(lines)):
            if lines[i][1] == data["username"] and lines[i][2] == passwordHash:
                controllo = 1
                # Criteri della password
                policy = PasswordPolicy.from_names(
                    length=8,  # min length: 8
                    uppercase=1,  # need min. 1 uppercase letters
                    numbers=1,  # need min. 1 digits
                    special=1,  # need min. 1 special characters
                    nonletters=1,  # need min. 1 non-letter characters (digits, specials, anything)
                )
                while True:
                    password1 = getpass.getpass(
                        "Password must contain:\n- 8 Character\n- Number\n- Uppercase character\n- Special character\nPassword: ")
                    if len(policy.test(password1)) == 0:
                        # Password strength
                        passwordStrength(password1)
                        password2 = getpass.getpass("Confirm password: ")
                        if password1 == password2:
                            passwordHash = hashlib.sha256(password1.encode('utf-8')).hexdigest()
                            lines[i][2] = passwordHash
                            writer = csv.writer(open('userDB.csv', 'w'), delimiter='|')
                            writer.writerows(lines)
                            break
                        else:
                            print("Password doesn't match!")
                    print("")
        if controllo == 1:
            print("Password was change successful!\n")
            exit()
        else:
            print("Invalid credential...\n")
