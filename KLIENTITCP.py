import socket
#Deklarimi i 'serverName' dhe 'port' dhe mundesia per t'u inicializuar ato nga perdoruesi

while True:
    serverName = 'localhost'
    serverPort = 13000

    print("Deshironi te ndryshoni emrin e serverit dhe portin?\n " + 
          "Shtyp 'P' per PO, shtyp 'J' per JO \n")
    noYesInput = input("Zgjedhja: ")
    noYesInput = noYesInput.upper()
    if noYesInput == "P":
        serverName = input("Emri i serverit: ")
        port = input("Porti: ")
        serverPort = int(port)
    elif noYesInput == "J":
        print("Mbesin vlerat e meparshme:\nEmriServerit: " + str(serverName) + " | Port: " + str(serverPort))
        
    #Krijimi i soketes
    try:
        soketa = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soketa.connect((serverName, serverPort))
        print("\nJeni konektuar, mund t'i dergoni kerkesa!")
        break
    except:
        print("Konektimi nuk u realizua! Provoni perseri... \n")

while True: 
    print("===========================================================================")
    print("\nZgjedhni nje nga operacionet duke shenuar emrin: (IPADDRESS, PORT, COUNT, ROLLTHEDICE, REVERSE, TIME, " + 
                                                              " \nPALINDROME, GAME, GCF, CONVERT, PRIME, QUIT!)")
                               
    
    clientInput = input('\nOperacioni i zgjedhur: ')
    clientInput = clientInput.upper()
    formatClientInput = clientInput.strip()
    formatClientInput = formatClientInput.upper()  
    
    if len(formatClientInput) > 0 and \
       len(formatClientInput) <= 128:
        soketa.sendall(str.encode(formatClientInput))
    if not formatClientInput:
        print("Shenoni nje kerkese!")
        continue
    if formatClientInput == "QUIT":
        print("U mbyll lidhja me serverin!")
        soketa.close()
        break

    response = str(soketa.recv(1024), "utf-8")
    print('Pergjigjja: ' + str(response))
