#! /usr/bin/python3.9

import subprocess
import csv

data = {"id":"",
        "username":"",
        "password":"",
        "email":"",
        "block":"",
        "firstTime":""}

def updateCSV():
    reader = csv.reader(open("userDB.csv"), delimiter='|')
    lines=list(reader)
    #print(lines)
    for i in range (len(lines)):
        #print(lines[i][1])
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
    #print("Update settings successful!")


def updateData():
    with open('userDB.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            # Trovo la riga col nome e lavoro su quella
            if row["username"] == data["username"]:
                data["email"] = row["email"]
                data["block"] = row["block"]
                data["firstTime"] = row["firstTime"]
                writer.writerow({})


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
    # Opzione
    # 0) mail register()
    # 1) mail forgotPassword()
    # 2) mail changePassword()

    import smtplib
    import random

    emailTool = "" #YOUR EMAIL
    passwordTool = "" #https://myaccount.google.com/apppasswords

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()  # Identifica noi stessi al mailserver
        smtp.starttls()  # Cript del traffico
        smtp.ehlo()
        smtp.login(emailTool, passwordTool)  # Login in gmail

        code = ""
        for i in range(5):
            code += chr(random.randint(33, 126))

        if opzione == 0:
            subject = "Register verification code"
            body = "Your register verification code is: {}".format(code)
        elif opzione == 1:
            subject = "Forgot password verification code"
            body = "Your forgot password verification code is: {}".format(code)
        else:
            subject = "Change password verification code"
            body = "Your change password verification code is: {}".format(code)

        msg = "Subject: {}\n\n{}".format(subject, body)

        # esito 0 -> tutto ok
        # esito 1 -> mail sbagliata
        # esito 2 -> codice errato
        esito = 0
        try:
            smtp.sendmail(emailTool, email, msg)
        except:
            esito = 1
            return esito

        verifyCode = input("Insert the code we sent you via email: ")

        if code == verifyCode:
            return esito
        else:
            esito = 2
            return esito



def loginRegisterMenu():
    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                 HELLO USER                    |")
    print("+-----------------------------------------------+")
    print("1) Login\n2) Register\n")

    # Scelta del opzione
    while True:
        x = input("Select option: ")
        try:
            x = int(x)
        except ValueError:
            print("Number please")
            continue
        if 1 <= x <= 2:
            break
        else:
            print("Select a valid option")

    if x == 1:
        login()
    else:
        register()


def login():
    import hashlib
    import getpass
    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                 LOGIN MENU                    |")
    print("+-----------------------------------------------+")
    print("1) Login\n2) Forgot password\n")

    # Scelta del opzione
    while True:
        x = input("Select option: ")
        try:
            x = int(x)
        except ValueError:
            print("Number please")
            continue
        if 1 <= x <= 2:
            break
        else:
            print("Select a valid option")

    if x == 1:
        subprocess.call('clear', shell=True)
        print("+-----------------------------------------------+")
        print("|                                               |")
        print("|                  HackTool                     |")
        print("|                                               |")
        print("+-----------------------------------------------+")
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
    import smtplib
    import hashlib
    from password_strength import PasswordPolicy
    import getpass
    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
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
                        password1 = getpass.getpass("Password must contain:\n- 8 Character\n- Number\n- Uppercase character\n- Special character\nPassword: ")
                        if len(policy.test(password1)) == 0:
                            # Password strength
                            passwordStrength(password1)
                            password2 = getpass.getpass("Confirm password: ")
                            if password1 == password2:
                                esito = sendMail(email,1)
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
    import hashlib
    import getpass
    import re
    from password_strength import PasswordPolicy

    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                  REGISTER                     |")
    print("+-----------------------------------------------+")

    # Scorro database dei nomi per vedere se il nome è gia registrato
    # Primary key [id]
    # Foreign key [username]

    #---Soluzione intelligente per database grandi-------------------------------
    # Controllo se l username non è presente
    userDB=[]
    id = 0
    with open('userDB.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            # Carico l'intero database colonna username in una lista
            userDB.append(row["username"])
            id+=1

    while True:
        username: str = input("Username: ")
        # Scorro la lista per vedere se il nome è gia usato in tal caso errore
        if username in userDB:
            print("Username already used!\n")
        else:
            break

    #---Soluzione intelligente per database piccoli--------------------------------
    # Funzional ma non troppo in quanto se nella password cifrata si presenta
    # lo username il programma dirà che il nome gia esiste

    #username = input('Enter username >')
    #if username in open('names.csv', 'r').read():
    #    print('Username already exists')
    #-----------------------------------------------------------------------------

    # Criteri della password
    policy = PasswordPolicy.from_names(
        length = 8,  # min length: 8
        uppercase = 1,  # need min. 1 uppercase letters
        numbers = 1,  # need min. 1 digits
        special = 1,  # need min. 1 special characters
        nonletters = 1,  # need min. 1 non-letter characters (digits, specials, anything)
    )
    while True:
        password1 = getpass.getpass("Password must contain:\n- 8 Character\n- Number\n- Uppercase character\n- Special character\nPassword: ")
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
    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                  SETTINGS                     |")
    print("+-----------------------------------------------+")
    data["firstTime"] = "0"
    updateCSV()
    print("1) Change password\n2) Back to menu\n")

    # Scelta del opzione
    while True:
        x = input("Select option: ")
        try:
            x = int(x)
        except ValueError:
            print("Number please")
            continue
        if 1 <= x <= 2:
            break
        else:
            print("Select a valid option")

    if x == 1:
        changePassword()
    else:
        mainMenu()

def changePassword():
    import hashlib
    from password_strength import PasswordPolicy
    import getpass

    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
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
                    password1 = getpass.getpass("Password must contain:\n- 8 Character\n- Number\n- Uppercase character\n- Special character\nPassword: ")
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


def mainMenu():
    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                    MENU                       |")
    print("+-----------------------------------------------+")
    print("1) Settings\n2) Exit\n")

    # Scelta del opzione
    while True:
        x = input("Select option: ")
        try:
            x = int(x)
        except ValueError:
            print("Number please")
            continue
        if 1 <= x <= 2:
            break
        else:
            print("Select a valid option")

    if x == 1:
        settings()
    else:
        exit()

loginRegisterMenu()
