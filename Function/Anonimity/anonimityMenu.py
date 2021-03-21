##############################
#                            #
#   IMPORT DELLE LIBRERIE    #
#                            #
##############################
from tkinter import *
#Menu
from Function.Main.mainMenu import *


def clear(object):
    object.destroy()


def anonimityMenu(cancobj):
    print("anonimity.py")
    clear(cancobj)
    root = Tk()
    root.geometry("400x600")
    root.title("HackTool")
    root.configure(background='grey')
    root.resizable(False, False)
    root.grid_columnconfigure(0, weight=1)

    ##############################
    #                            #
    #      DISEGNO DEL MENU      #
    #                            #
    ##############################
    title = Label(root, text="HackTool", bg="grey", fg="white")
    title.config(font=('helvetica', 30))
    title.grid(row=0, column=0, padx=20, pady=40)

    # subprocess.call('arp -r', shell=True)
    macspoofingbtn = Button(root, text="MACSPOOFING", bg="#474747", fg="white", height=2, width=20)
    macspoofingbtn.grid(row=10, column=0, sticky="N", padx=20, pady=0)

    hostnamebtn = Button(root, text="HOSTNAME", bg="#474747", fg="white", height=2, width=20)
    hostnamebtn.grid(row=10, column=0, sticky="N", padx=10, pady=50)

    dnsbtn = Button(root, text="DNS", bg="#474747", fg="white", height=2, width=20)
    dnsbtn.grid(row=10, column=0, sticky="N", padx=10, pady=100)

    proxybtn = Button(root, text="PROXY", bg="#474747", fg="white", height=2, width=20)
    proxybtn.grid(row=10, column=0, sticky="N", padx=10, pady=150)

    vpnbtn = Button(root, text="VPN", bg="#474747", fg="white", height=2, width=20)
    vpnbtn.grid(row=10, column=0, sticky="N", padx=10, pady=200)

    backtomenubtn = Button(root, text="BACK TO MENU", bg="#8a0000", fg="white", height=2, width=20, command= lambda: mainMenu(root))
    backtomenubtn.grid(row=10, column=0, sticky="N", padx=10, pady=330)
    ###################################################################################################
    root.mainloop()