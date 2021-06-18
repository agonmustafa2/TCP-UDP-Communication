import sys
import socket
import datetime
import random
from _thread import *
import math

serverName = 'localhost'
serverPort = 13000
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Gabimi gjate krijimit te soketes: " + str(msg))

try:
    print("Serveri eshte startuar ne " + str(serverName) + " ne portin: " + str(serverPort))
    print("Lidhja me portin " + str(serverPort) + "!")
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(5)
    print("Serveri eshte i gatshem te pranoj kerkesa!" + "\n")
except socket.error as msg:
    print("Gabimi gjate startimit te serverit: " + str(msg))

def IPADDRESS():
    return "IP adresa e klientit eshte: " + str(address[0])

def PORT(porti):
    return "Klienti eshte duke perdorur portin " + porti
 
def COUNT(stringu):
    numriZanore = 0
    numriBashketingellore = 0
    zanore = [ 'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y' ]; 
    for i in stringu:
        if i.isalpha():
            if i not in zanore:
                numriBashketingellore += 1
            elif i in zanore:
                numriZanore += 1
    return str("Teksti i pranuar permban " + str(numriZanore) + " zanore dhe " + str(numriBashketingellore) + " bashketingellore!")
 
def ROLLTHEDICE():
    min = 1
    max = 6
    
    roll = "yes"
    while roll == "yes" or roll == "y":
        return random.randint(min, max)


def REVERSE(fjala):
    fjala = str(fjala)
    fjalar = fjala[::-1]
    return str(fjalar)


def TIME():
    koha = datetime.datetime.now()
    return koha.strftime("%H:%M:%S %p")

def PALINDROME(fjala):
    fjala = str(fjala)
    fjalar = fjala[::-1]
    if fjala == fjalar:
        return str("Fjala e shenuar eshte PALINDROME!")
    else:
        return str("Fjala e shenuar nuk eshte PALINDROME!")

def GAME(): 
    randomNumbers = [] 
    for iterator in range(5): 
        randomNumbers.append(random.randint(1, 35)) 
        randomNumbers.sort()
    return randomNumbers

def GCF(nr1, nr2):
    nr1 = int(nr1)
    nr2 = int(nr2)
    if(nr2==0): 
        return nr1 
    else: 
        return GCF(nr2,nr1%nr2)

def CONVERT(opsioni, numri):
    numri = float(numri)
    if opsioni == "CMTOFEET":
        return numri / 30.48
    elif opsioni == "FEETOCM":
        return numri * 30.48
    elif opsioni == "KMTOMILES":
        return numri / 1.609
    elif opsioni == "MILESTOKM":
        return numri * 1.609 

def PRIME(num):
    if num > 1:
   # KONTROLLO PER FAKTORE
        for i in range(2,num):
            if (num % i) == 0:
                return str(str(num) + str("nuk eshte numer prim"))
                return str(str(i) + str("times") + (num//i) + str("is") + str(num))
                break
        else:
            return str(str(num) + str(" eshte numer prim"))
       
        # NESE NUMRI INPUTIT ESHTE ME I VOGEL
        # OSE I BARABARTE ME 1 , NUK ESHTE PRIM
    else:
        return str(str(num) + str(" nuk eshte numer prim"))

def clientThread(connection, address):
    while True:
        try:
            client_response = str(connection.recv(1024), "utf-8")
            print("Kerkesa e klientit " + str(address[0]) + " eshte: " + str(client_response))
            client_response = client_response.split(" ")
            sendResponse = str("")
            if client_response[0] == "IPADDRESS":
                sendResponse = str(IPADDRESS())
            elif client_response[0] == "PORT":
                sendResponse = str(PORT(str(address[1])))
            elif client_response[0] == "COUNT": 
                stringuPerCount=""
                stringuPerCount = str.join(" ", client_response[1:])
                sendResponse = str(COUNT(stringuPerCount))
            elif client_response[0] == "ROLLTHEDICE":
                sendResponse = str(ROLLTHEDICE())
            elif client_response[0] == "REVERSE":
                sendResponse = str(REVERSE(client_response[1]))
            elif client_response[0] == "TIME":
                sendResponse = str(TIME())
            elif client_response[0] == "PALINDROME":   
                sendResponse = str(PALINDROME(client_response[1]))
            elif client_response[0] == "GAME":
                sendResponse = str(GAME())
            elif client_response[0] == "GCF":
                sendResponse = str(GCF(client_response[1], client_response[2]))
            elif client_response[0] == "CONVERT":
                sendResponse = str(CONVERT(client_response[1], client_response[2]))
            elif client_response[0] == "PRIME":
                sendResponse = str(PRIME(int(client_response[1])))
            elif client_response[0] == "QUIT":
                print("Klienti " + str(address[0]) + " nuk eshte ne linje!")
                break
            else:
                sendResponse = str("Kerkesa nuk egziston! Provoni perseri...")
        except IndexError:
            sendResponse = str("Nuk keni dhene argumentet e duhura! Provoni perseri...")
             
        connection.send(str.encode(sendResponse))
    connection.close()

while 1:
    connection, address = serverSocket.accept()
    print("\nKerkesa per konektim u pranua! Ne linje eshte: | IP: " + str(address[0]) + " | Port: " + str(address[1]))
    start_new_thread(clientThread, (connection, address))
