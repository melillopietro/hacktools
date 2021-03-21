#! /usr/bin/python3.9

from utilityFunction import disegno, scelta, backToMenu

def checkInternetConnection():
    disegno()
    print("|           CHECK INTERNET CONNECTION           |")
    print("+-----------------------------------------------+")
    import urllib.request

    try:
        urllib.request.urlopen('http://google.com')
        conn = True
    except:
        conn = False
    if conn:
        print('You are connected to the internet\n')
    else:
        print('You are NOT connected to the internet\n')
    backToMenu()


def speedTest():
    disegno()
    print("|                   SPEED TEST                  |")
    print("+-----------------------------------------------+")
    import speedtest
    print("Inizio speed test in corso...\n")
    print("Ricerca miglior server...")
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    print("Server migliore trovato\n\nTest Download...")
    s.download()
    print("Test Upload...\n")
    s.upload()
    res = s.results.dict()
    print("+-----------------------------------------------+")
    print("|                   Risultati                   |")
    print("+-----------------------------------------------+")
    print("             Download [{:.2f}] Kb/s".format(res["download"] / 1024))
    print("             Upload [{:.2f}] Kb/s".format(res["upload"] / 1024))
    print("             Ping [{:.0f}]".format(res["ping"]))
    print("+-----------------------------------------------+")
    backToMenu()


def nmapMenu():
    disegno()
    print("|                   NMAP MENU                   |")
    print("+-----------------------------------------------+")
    print("1) Net scan\n2) OS scan")
    x = scelta(1, 2)
    if x == 1:
        nmap()
    else:
        os()


def nmap():
    disegno()
    print("|                     NMAP                      |")
    print("+-----------------------------------------------+")
    import nmap3
    import json
    ip = input("Insert specific IP or \"<IP>/24\" for entire network: ")
    print("Port range:\n1) Default \"1-100\"\n2) Custom\n3) All")
    x = scelta(1, 3)
    if x == 1:
        port = "1-100"
    elif x == 2:
        rangemin = input("Port range min: ")
        rangemax = input("Port range max: ")
        port = str(rangemin) + "-" + str(rangemax)
    else:
        port = "1-65535"
    print("\n")

    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(ip, args="-p" + port)

    # Creo file json [report] con i dati di results
    report = json.dumps(results, sort_keys=True)

    # Trasformo da json in a dizionario
    data = json.loads(report)

    testo = ""

    # Stampo il dizionario
    for i, info in data.items():
        testo += "Scanned IP [{}]\n".format(i)
        for categoria, dizionario in info.items():
            if categoria == "hostname":
                if len(dizionario) != 0:
                    for dettaglio, valoreDettaglio in dizionario[0].items():
                        testo += "{} : {}\n".format(dettaglio, valoreDettaglio)
                else:
                    testo += "name : Not identified\ntype : Not identified\n"
            elif categoria == "ports":
                testo += "PORT       PROTOCOL       SERVICE        STATUS\n"
                for dettaglio in dizionario:
                    for porta, valorePorta in dettaglio.items():
                        if porta == "portid" or porta == "protocol" or porta == "state":
                            testo += "{:<13s}".format(valorePorta)
                        if porta == "service":
                            testo += "{:<15s}".format(valorePorta["name"])
                    testo += "\n"
        testo += "\n"

    # Rinomino il file
    x = "MP_"
    x += ip.replace("/24", "_EN")
    x += "_port_" + str(port)
    wfile = open("./Nmap/MP/" + x + ".txt", "w")
    wfile.write(testo)
    wfile.close()
    print(testo)
    backToMenu()


def os():
    disegno()
    print("|                    NMAP OS                    |")
    print("+-----------------------------------------------+")
    import nmap3
    import json
    ip = input("Insert specific IP or \"<IP>/24\" for entire network: ")
    while True:
        scelta = input("Port to scan: ")
        try:
            scelta = int(scelta)
        except ValueError:
            print("Number please")
            continue
        if type(scelta) == int:
            break
        else:
            print("Select a valid option")
    port = str(scelta)
    print("\n")

    nmap = nmap3.Nmap()
    results = nmap.nmap_os_detection(ip)

    # Creo file json [report] con i dati di results
    report = json.dumps(results, sort_keys=True, indent=4)

    # Trasformo da json in a dizionario
    data = json.loads(report)

    stampa = False
    testo = ""
    testo1 = ""
    testo2 = ""
    testo3 = ""

    # Stampo il dizionario
    for i, info in data.items():
        testo1 += "Scanned IP [{}]\n".format(i)
        for categoria, dizionario in info.items():
            if categoria == "hostname":
                if len(dizionario) != 0:
                    for dettaglio, valoreDettaglio in dizionario[0].items():
                        testo1 += "{} : {}\n".format(dettaglio, valoreDettaglio)
                else:
                    testo1 += "name : Not identified\ntype : Not identified\n"
            elif categoria == "ports":
                testo3 += "\nPORT       PROTOCOL       SERVICE        STATUS\n"
                for dettaglio in dizionario:
                    for porta, valorePorta in dettaglio.items():
                        if valorePorta == port:
                            testo3 += "{:<13s}".format(valorePorta)
                            stampa = True
                        if stampa == True and porta == "protocol":
                            testo3 += "{:<13s}".format(valorePorta)
                        if stampa == True and porta == "service":
                            testo3 += "{:<15s}".format(valorePorta["name"])
                        if stampa == True and porta == "state":
                            testo3 += "{:<13s}".format(valorePorta)
                            stampa = False
                testo3 += "\n\n"
            elif categoria == "osmatch":
                testo2 = "Operative System: "
                for dettaglio in dizionario:
                    for os, valoreOS in dettaglio.items():
                        if os == "name":
                            testo2 += valoreOS + " "
                            stampa = True
                if stampa == False:
                    testo2 += "Not identified"
                stampa = False

            testo += testo1 + testo2 + testo3
            testo3 = ""
            testo2 = ""
            testo1 = ""

    # Rinomino il file
    x = "OS_"
    x += ip.replace("/24", "_EN")
    x += "_port_" + str(port)
    wfile = open("./Nmap/OS/" + x + ".txt", "w")
    wfile.write(testo)
    wfile.close()
    print(testo)
    backToMenu()


def netcut():
    disegno()
    print("|                    NETCUT                     |")
    print("+-----------------------------------------------+")
    backToMenu()


def jumperDNS():
    disegno()
    print("|                   JUMPERDNS                   |")
    print("+-----------------------------------------------+")
    backToMenu()