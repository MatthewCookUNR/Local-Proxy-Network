'''
Created on Dec 4, 2019

@author: Matthew Cook
'''

import sqlite3
from socket import socket, AF_INET, SOCK_STREAM
from ast import literal_eval
import traceback

########################### SERVER FUNCTIONS ###############################################################

#Name: REGISTER
#
#Purpose: Registers a device from database
#
#Param: in: string representing device's Id (deviceId)
#       in: string representing devices's MAC address (deviceMAC)
#       in: string representing devices's IP address (IP)
#       in: string representing devices's port number(port)
#
#Brief: Function checks to see if device is registered with given
#       information and then registers device if applicable
#
#ErrorsHandled: N/A
#
def REGISTER(deviceId, deviceMAC, IP, port):
    try:
        #First check if device is already in DB
        dbCursor.execute('SELECT * FROM devices WHERE name = ?', (deviceId, ))
        rows = dbCursor.fetchall()
        
        #If length of rows is 0, the given deviceId and MAC is currently not registered in DB
        if len(rows) == 0:
            #Insert device info into table
            dbCursor.execute('INSERT INTO devices(name, macAddress, IP, portNum) VALUES(?, ?, ?, ?)',
                              (deviceId, deviceMAC, IP, port))
            sqlConnection.commit()
            print(deviceId + " is registered in database")
            ACK((0 , "Your device is registered in DB" ))
        else:
            print(deviceId + " is already registered in database")
            ACK((0, "Your device is already registered in database"))
    except:
        print("Register in db unsuccessful")
        print(traceback.format_exc())
        NACK((1, str(e)))


#Name: DEREGISTER
#
#Purpose: Deregisters a device from database
#
#Param: in: string representing device's Id (deviceId)
#       in: string representing devices's MAC address (deviceMAC)
#
#Brief: Function checks to see if device is registered with given
#       information and then deregisters it if applicable
#
#ErrorsHandled: N/A
#
def DEREGISTER(deviceId, deviceMAC):
    try:
        #First check if device is already in DB
        dbCursor.execute('SELECT * FROM devices WHERE name = ? AND macAddress = ?',
                          (deviceId, deviceMAC ))
        rows = dbCursor.fetchall()
        
        #If length of rows is 0, the given deviceId is currently not registered in DB
        if len(rows) == 0:
            #Insert device info into table
            print("Device is not registered in the database")
            ACK((0, "Your device is not registered in the database"))
        else:
            dbCursor.execute('DELETE FROM devices WHERE name = ?', (deviceId, ))
            sqlConnection.commit()
            print(deviceId + " is deregistered in database")
            ACK((0, "Your device is now deregistered in database"))
        
    except:
        print("Deregister in db unsuccessful")
        print(traceback.format_exc())
        NACK((1, str(e)))

#Name: MSG
#
#Purpose: Adds message to the mailbox table in database
#
#Param: in: string representing sender's Id (senderId)
#       in: string representing receiver's Id (receiverId)
#       in: string message being sent (message)
#
#Brief: Stores message as mail in the mailbox table and then
#       sends the user a ACK.
#
#ErrorsHandled: Checks to make sure that both receiver and sender
#               exist as registered devices
#
def MSG(senderId, receiverId, message):
    try:
        print("Adding message from " + senderId + " to " + receiverId)
        dbCursor.execute('SELECT * FROM devices WHERE name = ?', (senderId, ))
        result = dbCursor.fetchall()
        if len(result) == 0:
            NACK((1, "Your ID is not registered in database"))
            return
            
        dbCursor.execute('SELECT * FROM devices WHERE name = ?', (receiverId, ))
        result = dbCursor.fetchall()
        if len(result) == 0:
            NACK((1, "Receiver Id is not registered in database"))
            return
        
        dbCursor.execute('INSERT INTO mailbox(toId, fromId, message, timestamp) VALUES(?, ?, ?, datetime("now"))',
                          (receiverId, senderId, message) )
        sqlConnection.commit()
        ACK((0, "Message was saved in the database"))
        
    except:
        print("Message saved unsuccessfully")
        print(traceback.format_exc())
        NACK((1, "Error occurred while saving message"))
        
#Name: QUERY
#
#Purpose: Query database for desired information
#
#Param: in: string representing device's Id (deviceId)
#
#Brief: Query database for information requested by the client
#       Right now queries mailbox for messages to the client
#
#ErrorsHandled: 
#
def QUERY(qType, deviceId):
    if qType is 0:
        try:
            print("Querying mailbox for " + deviceId)
            dbCursor.execute('SELECT * FROM mailbox WHERE toId = ? ORDER BY id DESC', (deviceId, ))
            result = dbCursor.fetchall()
            ACK((0, "Here is your mail", result))
        except:
            print("Query unsuccessful")
            print(traceback.format_exc())
            NACK((1, "Error occurred while querying your mail")) 
    elif qType is 1:
        try:
            print("Querying server for " + deviceId)
            dbCursor.execute('SELECT * FROM devices WHERE name = ?', (deviceId, ))
            result = dbCursor.fetchall()
            if len(result) == 0:
                result = None
                ACK((0, "Device is not currently registered", result))
            else:
                ACK((0, "Device is registered currently", result))
        except:
            print("Query unsuccessful")
            print(traceback.format_exc())
            NACK((1, "Error occurred while querying your mail")) 

#Name: ACK
#
#Purpose: Sends ACK message to client
#
#Param: in: string representing ACK message (response)
#
#Brief: Sends ACK message that lets client know their
#       request has been completed successfully
#
#ErrorsHandled: N/A
#
def ACK(response):
    response = str.encode(str(response))
    print("Sending ACK")
    clientConnect.send(response)        

#Name: NACK
#
#Purpose: Sends NACK message to client
#
#Param: in: string representing NACK message (response)
#
#Brief: Sends NACK message that lets client know their
#       request was completed unsuccessfully
#
#ErrorsHandled: N/A
#
def NACK(response):
    response = str.encode(str(response))
    print("Sending NACK")
    clientConnect.send(response)     
    
#Name: Clean Up Mail
#
#Purpose: Deletes mail for given device id
#
#Param: in: string representing device's Id (deviceId)
#
#Brief: Test function that removes mail from a desired
#       device
#
#ErrorsHandled: N/A
#       
def cleanUpMail(deviceId):
    dbCursor.execute('DELETE FROM mailbox WHERE toId = ?', (deviceId, )) 
    sqlConnection.commit() 
    
####################### MAIN PROGRAM #######################################################################
    
#Connecting to SQLite Database
print("Setting up SQLite db")
sqlConnection = sqlite3.connect('Proxy_Data.db')
dbCursor = sqlConnection.cursor()
dbCursor.execute('CREATE TABLE IF NOT EXISTS devices (id INTEGER PRIMARY KEY, name TEXT, macAddress TEXT, IP TEXT, portNum TEXT)')
dbCursor.execute('CREATE TABLE IF NOT EXISTS mailbox (id INTEGER PRIMARY KEY, toId TEXT, fromId TEXT, message TEXT, timestamp TEXT)')
print("Db connected")

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
            REGISTER(recvData[1], recvData[2], addr[0], addr[1])
        elif recvData[0] is 2: #Deregister request
            DEREGISTER(recvData[1], recvData[2])
        elif recvData[0] is 3: #MSG received
            MSG(recvData[1], recvData[2], recvData[3])
        elif recvData[0] is 4:
            QUERY(recvData[1], recvData[2])
        elif recvData[0] is 5:
            print("5")
        elif recvData[0] is 6:
            print("6")        
        else:
            print("Malformed Packet Detected")