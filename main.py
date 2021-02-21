#! /usr/bin/python3.9

############################################
#                                          #
#       Update csv                         #
#       Rifare crittografia (debole)       #
#       Recupero password                  #
#       2FA                                #
#                                          #
############################################

import subprocess
import csv

data = {"id":"",
        "username":"",
        "email":"",
        "block":"",
        "firstTime":""}

def updateCSV():
    with open('userDB.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        writer = csv.DictWriter(csvfile, delimiter='|')
        for row in reader:
            # Trovo la riga col nome e lavoro su quella
            if row["username"] == data["username"]:
                row["email"] = data["email"]
                row["block"] = data["block"]
                row["firstTime"] = data["firstTime"]
    writer.writerow(row)

def updateData():
    with open('userDB.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            # Trovo la riga col nome e lavoro su quella
            if row["username"] == data["username"]:
                data["email"] = row["email"]
                data["block"] = row["block"]
                data["firstTime"] = row["firstTime"]


def loginRegisterMenu():
    subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                 HELLO USER                    |")
    print("+-----------------------------------------------+")
    print("1) Login\n2) Forgot password\n3) Register\n")

    # Scelta del opzione
    while True:
        x = input("Select option: ")
        try:
            x = int(x)
        except ValueError:
            print("Number please")
            continue
        if 1 <= x <= 3:
            break
        else:
            print("Select a valid option")

    if x == 1:
        login();
    elif x == 2:
        forgotPassword()
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
                    data["email"] = row["email"]
                    data["block"] = row["block"]
                    data["firstTime"] = row["firstTime"]
                    if data["firstTime"]=="1":
                        settings()
                    else:
                        mainMenu()
            exit()
            print("Invalid credential...\n")
            error += 1
            if error == 3:
                print("Sorry we must block you!")
                exit()


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

    while True:
        password1 = getpass.getpass("Password: ")
        password2 = getpass.getpass("Confirm password: ")
        if password1 == password2:
            #############################
            # How strong is my password #
            #############################
            passwordHash = hashlib.sha256(password1.encode('utf-8')).hexdigest()
            wfile = open("userDB.csv", "a")
            wfile.write(str(id)+"|"+username+"|"+passwordHash+"|"+email+"|0|1\n")
            wfile.close()

            login()
        else:
            print("Password doesn't match!\n")


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
    print(data)
    data["firstTime"] = "0"
    #updateCSV()


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