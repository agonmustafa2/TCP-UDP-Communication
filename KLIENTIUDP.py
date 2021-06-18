import socket
#Deklarimi i 'serverName' dhe 'port' dhe mundesia per t'u inicializuar ato nga perdoruesi


serverName = 'localhost'
serverPort = 13000
print("Deshironi te ndryshoni emrin e serverit dhe portin?\n " + 
      "Shtyp 'P' per PO, shtyp 'J' per JO \n")
noYesInput = input("Zgjedhja: ")
noYesInput = noYesInput.upper()
if noYesInput == "P":
    serverName = input("Emri i serverit: ")
    port = input("Porti per qasje: ")
    serverPort = int(port)
elif noYesInput == "J":
    print("Mbesin vlerat e nenkuptuara:\nEmriServerit: " + str(serverName) + " | Port: " + str(serverPort))
        
#Krijimi i soketes
soketa = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("\nMund te dergoni kerkesa!")

while True:
    print("===========================================================================")
    print("\nZgjedhni nje nga operacionet duke shenuar emrin: (IPADDRESS, PORT, COUNT, ROLLTHEDICE, REVERSE, TIME, " + 
                                                              " \nPALINDROME, GAME, GCF, CONVERT, PRIME, QUIT!)")
 
    clientInput = input('\nOperacioni i zgjedhur: ')
    formatClientInput = clientInput.strip()
    formatClientInput = formatClientInput.upper()  
    
    if len(formatClientInput) > 0 and \
       len(formatClientInput) <= 128:
        soketa.sendto(formatClientInput.encode(), (serverName, serverPort))
        response = soketa.recv(128)
        response = response.decode('utf-8')
        print('Pergjigjja: ' + str(response))
    if not formatClientInput:
        print("Shenoni nje kerkese!")
        continue
    if formatClientInput == "QUIT":
        print("U mbyll lidhja me serverin!")
        soketa.close()
        break
