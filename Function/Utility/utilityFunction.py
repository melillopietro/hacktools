#! /usr/bin/python3.9
import subprocess

def backToMenu():
    while True:
        x = input("Do you continue [Y / N]: ").lower()
        if x == "y":
            #mainMenu()
            break
        elif x == "n":
            exit()
        else:
            print("Select a valid option")


def disegno():
    subprocess.call('clear', shell=True)
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
