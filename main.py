#! /usr/bin/python3.9

############################################
#                                          #
#       Rifare crittografia (debole)       #
#       Recupero password                  #
#       2FA                                #
#                                          #
############################################

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
    for i in range (len(lines)):
        #print(lines[i][1])
        if lines[i][1] == data["username"]:
            lines[i][2] = data["password"]
            lines[i][3] = data["email"]
            lines[i][4] = data["block"]
            lines[i][5] = data["firstTime"]
            writer = csv.writer(open('userDB.csv', 'w'), delimiter='|')
            writer.writerows(lines)
            ##############################
            #    DA ERRORE MA FUNZIONA   #
            ##############################
    print("Update settings successful!")

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
    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|               FORGOT PASSWORD                 |")
    print("+-----------------------------------------------+")


def register():
    import hashlib
    import getpass
    import re
    from password_strength import PasswordPolicy, PasswordStats
    import smtplib

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
    # Controllo formale email
    while True:
        email = input("Email: ")
        if "." in email and "@" in email:
            break
        else:
            print("Invalid email!\n")

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
            stats = PasswordStats(password1)
            strength=round(stats.strength(),3)
            x="Password strength [{}/0.999] -> ".format(strength)
            if 0.0 <= strength and strength <= 0.333:
                x += "[weak]"
            elif 0.334 <= strength and strength <= 0.666:
                x += "[medium]"
            else:
                x += "[strong]"
            print(x)
            password2 = getpass.getpass("Confirm password: ")
            if password1 == password2:
                passwordHash = hashlib.sha256(password1.encode('utf-8')).hexdigest()

                # MAIL DI CONFERMA
                import smtplib
                import random

                emailTool = "hacktoolits@gmail.com"
                passwordTool = "efwhdqqmqelsghsy"

                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()  # Identifica noi stessi al mailserver
                    smtp.starttls()  # Cript del traffico
                    smtp.ehlo()
                    smtp.login(emailTool, passwordTool)  # Login in gmail

                    code = ""
                    for i in range(5):
                        code += chr(random.randint(33, 126))

                    subject = "Verification code"
                    body = "Verification code: {}".format(code)
                    msg = "Subject: {}\n\n{}".format(subject, body)
                    smtp.sendmail(emailTool, email, msg)

                    verifyCode = input("Insert the code we sent you via email: ")
                    if code == verifyCode:
                        wfile = open("userDB.csv", "a")
                        wfile.write(str(id) + "|" + username + "|" + passwordHash + "|" + email + "|0|1\n")
                        wfile.close()

                        login()
                    else:
                        pass
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
    #print(data)
    #print("")
    data["firstTime"] = "0"
    updateCSV()


def mainMenu():
    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                    MENU                       |")
    print("+-----------------------------------------------+")


loginRegisterMenu()