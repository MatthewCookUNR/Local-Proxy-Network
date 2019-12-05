'''
Created on Dec 4, 2019

@author: Matthew Cook
'''
from socket import socket, AF_INET, SOCK_STREAM
from ast import literal_eval

def REGISTER(deviceId, deviceMAC):
    print(deviceId + " is registered in database")
    ACK()
    
def DEREGISTER(deviceId):
    print(deviceId + " is no longer registered in database")
    ACK()
    
def ACK():
    myMessage = (1, "Data Feedback")
    myMessage = str.encode(str(myMessage))
    print("Sending ACK")
    clientConnect.send(myMessage)        
    
def NACK():
    myMessage = (0, "Data Feedback")
    myMessage = str.encode(str(myMessage))
    print("Sending NACK")
    clientConnect.send(myMessage)  
    
#Socket Setup Code
TCPsocket = socket(AF_INET, SOCK_STREAM)
print ("Socket Created")
myIP = "192.168.56.1"
myPortNumber = 9999
TCPsocket.bind((myIP, myPortNumber))
TCPsocket.listen(5)
print("Waiting for connection" + "\n")
clientConnect, addr = TCPsocket.accept()
print ('Got a connection from', str(addr))
OPEN = True
while OPEN is True:
    recvData = clientConnect.recv(1024)
    recvData = bytes.decode(recvData)
    if recvData:
        recvData = literal_eval(recvData)
        if recvData[0] is 0: 
            print("0")
        elif recvData[0] is 1: #Register request
            print("I got a register message")
            REGISTER(recvData[1], recvData[2])
        elif recvData[0] is 2: #Deregister request
            DEREGISTER(recvData[1])
        elif recvData[0] is 3:
            print("3")
        elif recvData[0] is 4:
            print("4")
        elif recvData[0] is 5:
            print("5")
        elif recvData[0] is 6:
            print("6")        
        else:
            print("Malformed Packet Detected")