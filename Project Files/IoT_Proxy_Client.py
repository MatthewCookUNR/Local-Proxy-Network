'''
Created on Dec 4, 2019

@author: Matthew Cook
'''
from socket import socket
from uuid import getnode
from ast import literal_eval

#Client Functions

def REGISTER(deviceId):
    myMAC = getnode() #gets the MAC address of device
    myMAC = hex(myMAC)
    myMAC = myMAC[2:] # removes '0x' from the hexadecimal number
    myMAC = ':'.join(format(s, '02x') for s in bytes.fromhex(myMAC)) #seperates hexadecimal into MAC address form 
    myMessage = (1, deviceId, myMAC)                                 #(borrowed from stackoverflow)
    myMessage = str.encode(str(myMessage))
    socketTCP.send(myMessage) 
    recvData = socketTCP.recv(1024)
    recvData = bytes.decode(recvData)
    recvData = literal_eval(recvData)
    print("Register ACK received") #Placeholder for response based on Server
    print(recvData[1]) 

def DEREGISTER(deviceId):
    myMessage = (2, deviceId)
    myMessage = str.encode(str(myMessage))
    socketTCP.send(myMessage)
    recvData = socketTCP.recv(1024)
    recvData = bytes.decode(recvData)
    recvData = literal_eval(recvData)
    print("Deregister ACK received") #Placeholder for response based on Server
    
#Code for client to connect to server
socketTCP = socket()
myIP = "192.168.56.1"
myPortNumber = 9999
socketTCP.connect((myIP, myPortNumber))

#Client Information
userId = "Kamran's Tower"

#Client Functions Testing
REGISTER(userId) 
DEREGISTER(userId)