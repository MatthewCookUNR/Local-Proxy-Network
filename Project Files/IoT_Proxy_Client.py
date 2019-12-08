'''
Created on Dec 4, 2019

@author: Matthew Cook
'''
from socket import socket
from uuid import getnode
from ast import literal_eval

########################### CLIENT FUNCTIONS ###############################################################

#Name: REGISTER
#
#Purpose: Sends request to be registered
#
#Param: in: string representing device's Id (deviceId)
#
#Brief: Sends message to the server to request that device
#       be registered in proxy network
#
#ErrorsHandled: N/A
#
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
    if recvData[0] is 0: #Received message is a ACK
        print("ACK: " + recvData[1])
    elif recvData[0] is 1: #Received message is a NACK
        print("NACK: " + recvData[1])


#Name: DEREGISTER
#
#Purpose: Sends request to be deregistered
#
#Param: in: string representing device's Id (deviceId)
#
#Brief: Sends message to server so that it can handle removing
#       device register from proxy network
#
#ErrorsHandled: N/A
#      
def DEREGISTER(deviceId):
    myMAC = getnode() #gets the MAC address of device
    myMAC = hex(myMAC)
    myMAC = myMAC[2:] # removes '0x' from the hexadecimal number
    myMAC = ':'.join(format(s, '02x') for s in bytes.fromhex(myMAC)) #seperates hexadecimal into MAC address form 
    myMessage = (2, deviceId, myMAC)               
    myMessage = str.encode(str(myMessage))
    socketTCP.send(myMessage)
    recvData = socketTCP.recv(1024)
    recvData = bytes.decode(recvData)
    recvData = literal_eval(recvData)
    if recvData[0] is 0: #Received message is a ACK
        print("ACK: " + recvData[1])
    elif recvData[0] is 1: #Received message is a NACK
        print("NACK: " + recvData[1])

#Name: MSG
#
#Purpose: Sends message to another device in the network
#
#Param: in: string representing device's Id (deviceId)
#       in: string representing receiver's Id (receiverId)
#       in: string message being sent (message)
#
#Brief: Sends message to the server so that it can be stored in
#       the mailbox table of database
#
#ErrorsHandled: N/A/
#
def MSG(deviceId, receiverId, message):
    myMessage = (3, deviceId, receiverId, message)
    myMessage = str.encode(str(myMessage))
    socketTCP.send(myMessage)
    recvData = socketTCP.recv(1024)
    recvData = bytes.decode(recvData)
    recvData = literal_eval(recvData)
    if recvData[0] is 0: #Received message is a ACK
        print("ACK: " + recvData[1])
    elif recvData[0] is 1:#Received message is a NACK
        print("NACK: " + recvData[1])
      
#Name: QUERY
#
#Purpose: Query database for desired information
#
#Param: in: integer representing type of query
#       in: string representing device's Id (deviceId)
#
#Brief: Query database for desired information requested by 
#       the client
#
#ErrorsHandled: 
#  
def QUERY(type, deviceId):
    if type is 0:
        print("Mailbox Query")
        myMessage = (4, deviceId)
        myMessage = str.encode(str(myMessage))
        socketTCP.send(myMessage)
        recvData = socketTCP.recv(1024)
        recvData = bytes.decode(recvData)
        recvData = literal_eval(recvData)
        if recvData[0] is 0: #Received message is a ACK
            print("ACK: " + recvData[1])
            printQuery(recvData[2])

        elif recvData[0] is 1:#Received message is a NACK
            print("NACK: " + recvData[1]) 
    else:
        print("Inputted type is not a valid query type")

#Name: Print Query
#
#Purpose: Prints the result of a database query
#
#Param: in: 2-D Array representing database query (result)
#       in: string representing device's Id (deviceId)
#
#Brief: N/A
#
#ErrorsHandled: N/A
#  
def printQuery(result):
    for row in result:
        print(row)

####################### MAIN PROGRAM #######################################################################
    
#Code for client to connect to server
socketTCP = socket()
myIP = "192.168.56.1"
myPortNumber = 9999
socketTCP.connect((myIP, myPortNumber))

#Client Information
userId = "Kamran's Tower"
userId2 = "Nope"

#Client Functions Testing
REGISTER(userId) 
REGISTER(userId2)
MSG(userId, userId2, "Testing test")
QUERY(0, userId2)