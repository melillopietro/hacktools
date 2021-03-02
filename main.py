#! /usr/bin/python3.9

# Librerie main

# Import parti di codice
from loginRegisterFunction import *
from diagnosticFunction import *
from anonymityFunction import *
from whoisFunction import *
from hashFunction import *
from emailFunction import *

global data
data = {"id": "",
        "username": "",
        "password": "",
        "email": "",
        "block": "",
        "firstTime": ""}


def backToMenu():
    while True:
        x = input("Do you continue [Y / N]\n")
        try:
            x = int(x)
        except ValueError:
            print("Number please")
            continue
        if min <= x <= max:
            return x
        else:
            print("Select a valid option")
    mainMenu()


def disegno():
    #subprocess.call('clear', shell=True)
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                  HackTool                     |")
    print("|                                               |")
    print("+-----------------------------------------------+")


def scelta(min, max):
    while True:
        x = input("Select option: ")
        try:
            x = int(x)
        except ValueError:
            print("Number please")
            continue
        if min <= x <= max:
            return x
        else:
            print("Select a valid option")


def errorHandler():
    print("Qualcosa e' andato storto...")


def mainMenu():
    disegno()
    print("|                    MENU                       |")
    print("+-----------------------------------------------+")
    print("1) Diagnostic\n2) Anonymity\n3) Whois\n4) Hash\n5) Mail\n6) Settings\n7) Exit\n")
    x = scelta(1, 7)
    opzioni = {
        1: diagnostic,
        2: anonymity,
        3: whois,
        4: hash,
        5: mail,
        6: settings
    }
    if x == 7:
        exit()
    output = opzioni.get(x, errorHandler)()


def diagnostic():
    disegno()
    print("|                 DIAGNOSTIC                    |")
    print("+-----------------------------------------------+")
    print("1) Check internet connection\n2) Speed test\n3) Nmap\n4) Netcut\n5) Jumper DNS\n6) Back to menu\n")
    x = scelta(1, 6)
    opzioni = {
        1: checkInternetConnection,
        2: speedTest,
        3: nmapMenu,
        4: netcut,
        5: jumperDNS,
        6: mainMenu
    }
    output = opzioni.get(x, errorHandler)()


def anonymity():
    disegno()
    print("|                   ANONYMITY                   |")
    print("+-----------------------------------------------+")
    print("1) MAC spoofing\n2) Hostname\n3) DNS\n4) Proxy\n5) VPN\n6) Back to menu\n")
    x = scelta(1, 6)
    opzioni = {
        1: MACspoofing,
        2: hostname,
        3: DNS,
        4: proxy,
        5: vpn,
        6: mainMenu
    }
    output = opzioni.get(x, errorHandler)()

def whois():
    disegno()
    print("|                     WHOIS                     |")
    print("+-----------------------------------------------+")
    print("1) Whois domain tool\n2) Whois MAC\n3) AbuseIPDB\n4) IPVoid\n5) Back to menu\n")
    x = scelta(1, 5)
    opzioni = {
        1: whoisDomainTool,
        2: whoisMAC,
        3: abuseIPDB,
        4: ipVoid,
        5: mainMenu
    }
    output = opzioni.get(x, errorHandler)()


def hash():
    disegno()
    print("|                     HASH                      |")
    print("+-----------------------------------------------+")
    print("1) Hash checker\n2) Virus total\n3) Hybrid analisys\n4) Down detector\n5) Back to menu\n")
    x = scelta(1, 5)
    opzioni = {
        1: hashChecker,
        2: virusTotal,
        3: hybridAnalisys,
        4: downDector,
        5: mainMenu
    }
    output = opzioni.get(x, errorHandler)()


def mail():
    disegno()
    print("|                    EMAIL                      |")
    print("+-----------------------------------------------+")
    print("1) Mail checker\n2) How strong is my password\n3) Mx toolbox\n4) Back to menu\n")
    x = scelta(1, 5)
    opzioni = {
        1: emailChecker,
        2: howStrongIsMyPassword,
        3: mxToolbox,
        4: mainMenu
    }
    output = opzioni.get(x, errorHandler)()

mainMenu()