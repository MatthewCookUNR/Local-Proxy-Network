'''
Created on Dec 4, 2019

@author: Matthew Cook
'''

import sqlite3
from socket import socket, AF_INET, SOCK_STREAM
from ast import literal_eval

#Server Functions
def REGISTER(deviceId, deviceMAC, IP, port):
    try:
        #First check if device is already in DB
        dbCursor.execute('SELECT * FROM devices WHERE name = ? AND macAddress = ?', (deviceId, deviceMAC))
        rows = dbCursor.fetchall()
        
        #If length of rows is 0, the given deviceId and MAC is currently not registered in DB
        if len(rows) == 0:
            #Insert device info into table
            dbCursor.execute('INSERT INTO devices(name, macAddress, IP, portNum) VALUES(?, ?, ?, ?)', (deviceId, deviceMAC, IP, port))
            sqlConnection.commit()
            print(deviceId + " is registered in database")
            ACK()
        else:
            print(deviceId + " is already registered in database")
            ACK()
    except Exception as e:
        print("Register in db unsuccessful")
        print(e)
    
def DEREGISTER(deviceId):
    try:
        #First check if device is already in DB
        dbCursor.execute('SELECT * FROM devices WHERE name = ?', (deviceId, ))
        rows = dbCursor.fetchall()
        
        #If length of rows is 0, the given deviceId and MAC is currently not registered in DB
        if len(rows) == 0:
            #Insert device info into table
            print("Device is not registered in the database")
            ACK()
        else:
            dbCursor.execute('DELETE FROM devices WHERE name = ?', (deviceId, ))
            sqlConnection.commit()
            print(deviceId + " is deregistered in database")
            ACK()
        
    except Exception as e:
        print("Deregister in db unsuccessful")
        print(e)
    
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
    
    
#Connecting to SQLite Database
print("Setting up SQLite db")
sqlConnection = sqlite3.connect('Proxy_Data.db')
dbCursor = sqlConnection.cursor()
print("Db connected")

#One-time used DB operations
#dbCursor.execute('CREATE TABLE devices (id INTEGER PRIMARY KEY, name TEXT, macAddress TEXT)')
#dbCursor.execute('ALTER TABLE devices ADD portNum TEXT')

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

#Server will always be open while program is ran to receive requests from
#a potential client
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
            REGISTER(recvData[1], recvData[2], addr[0], addr[1])
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