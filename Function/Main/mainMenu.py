##############################
#                            #
#   IMPORT DELLE LIBRERIE    #
#                            #
##############################
from tkinter import *
#Menu
from Function.Anonimity.anonimityMenu import *


def clear(object):
    object.destroy()


def mainMenu(cancobj):
    print("mainMenu.py")
    ##############################
    #                            #
    #      DISEGNO DEL MENU      #
    #                            #
    ##############################
    clear(cancobj)
    root = Tk()
    root.geometry("400x600")
    root.title("HackTool")
    root.configure(background='grey')
    root.resizable(False, False)
    root.grid_columnconfigure(0, weight=1)

    title = Label(root, text="HackTool", bg="grey", fg="white")
    title.config(font=('helvetica', 30))
    title.grid(row=0, column=0, padx=20, pady=40)

    anonimitybtn = Button(root, text="ANONIMITY", bg="#474747", fg="white", height = 2, width = 20, command = lambda: anonimityMenu(root))
    anonimitybtn.grid(row=10, column=0, sticky="N", padx=20, pady=0)

    diagnosticbtn = Button(root, text="DIAGNOSTIC", bg="#474747", fg="white", height = 2, width = 20)
    diagnosticbtn.grid(row=10, column=0, sticky="N", padx=10, pady=50)

    emailbtn = Button(root, text="EMAIL", bg="#474747", fg="white", height = 2, width = 20)
    emailbtn.grid(row=10, column=0, sticky="N", padx=10, pady=100)

    hashbtn = Button(root, text="HASH", bg="#474747", fg="white", height = 2, width = 20)
    hashbtn.grid(row=10, column=0, sticky="N", padx=10, pady=150)

    whoisbtn = Button(root, text="WHOIS", bg="#474747", fg="white", height = 2, width = 20)
    whoisbtn.grid(row=10, column=0, sticky="N", padx=10, pady=200)

    settingsbtn = Button(root, text="SETTINGS", bg="#b05e00", fg="white", height = 2, width = 20)
    settingsbtn.grid(row=10, column=0, sticky="N", padx=10, pady=270)

    exitbtn = Button(root, text="EXIT", bg="#8a0000", fg="white", height = 2, width = 20, command = exit)
    exitbtn.grid(row=10, column=0, sticky="N", padx=10, pady=330)
    ###################################################################################################
    root.mainloop()