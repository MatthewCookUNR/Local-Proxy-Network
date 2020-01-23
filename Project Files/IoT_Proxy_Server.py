'''
Created on Dec 4, 2019

@author: Matthew Cook
'''

import sqlite3
from socket import socket, AF_INET, SOCK_STREAM
from ast import literal_eval
import traceback
import threading
from threading import Thread

########################### CLIENT THREADING ###############################################################

class clientThread(Thread):
    def __init__(self, number, mySock, address):
        self.mySock = mySock
        self.address = address
        Thread.__init__(self, name = "Thread " + str(number))
        print(self.getName() + " has been initialized\n")
    def run(self):
        OPEN = True
        while OPEN is True:
            recvData = self.mySock.recv(1024)
            recvData = bytes.decode(recvData)
            if recvData:
                recvData = literal_eval(recvData)
                if recvData[0] is 0: 
                    print("0")
                elif recvData[0] is 1: #Register request
                    REGISTER(recvData[1], recvData[2], addr[0], addr[1], self.mySock)
                elif recvData[0] is 2: #Deregister request
                    DEREGISTER(recvData[1], recvData[2], self.mySock)
                elif recvData[0] is 3: #MSG received
                    MSG(recvData[1], recvData[2], recvData[3], self.mySock)
                elif recvData[0] is 4: #Query request
                    QUERY(recvData[1], recvData[2], self.mySock)
                elif recvData[0] is 5:
                    print("5")
                elif recvData[0] is 6:
                    print("6")        
                else:
                    print("Malformed Packet Detected")
                    
class sharedDataLocks:
    def __init__(self):
        self.devicesLock = threading.RLock()
        self.mailLock = threading.RLock()

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
def REGISTER(deviceId, deviceMAC, IP, port, sock):
    try:
        #First check if device is already in DB
        myLocks.devicesLock.acquire(True)
        dbCursor.execute('SELECT * FROM devices WHERE name = ?', (deviceId, ))
        rows = dbCursor.fetchall()
        
        #If length of rows is 0, the given deviceId and MAC is currently not registered in DB
        if len(rows) == 0:
            
            #Insert device info into table
            dbCursor.execute('INSERT INTO devices(name, macAddress, IP, portNum) VALUES(?, ?, ?, ?)',
                              (deviceId, deviceMAC, IP, port))
            sqlConnection.commit()
            myLocks.devicesLock.release()
            print(deviceId + " is registered in database")
            ACK((0 , "Your device is registered in DB" ), sock)
        else:
            myLocks.devicesLock.release()
            print(deviceId + " is already registered in database")
            ACK((0, "Your device is already registered in database"), sock)
    except Exception as e:
        if(myLocks.devicesLock._is_owned()):
            myLocks.devicesLock.release()
        print("Register in db unsuccessful")
        print(traceback.format_exc())
        NACK((1, str(e)), sock)


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
def DEREGISTER(deviceId, deviceMAC, sock):
    try:
        #First check if device is already in DB
        myLocks.devicesLock.acquire(True)
        dbCursor.execute('SELECT * FROM devices WHERE name = ? AND macAddress = ?',
                          (deviceId, deviceMAC ))
        rows = dbCursor.fetchall()
        
        #If length of rows is 0, the given deviceId is currently not registered in DB
        if len(rows) == 0:
            #Insert device info into table
            myLocks.devicesLock.release()
            print("Device is not registered in the database")
            ACK((0, "Your device is not registered in the database"), sock)
        else:
            dbCursor.execute('DELETE FROM devices WHERE name = ?', (deviceId, ))
            sqlConnection.commit()
            myLocks.devicesLock.release()
            print(deviceId + " is deregistered in database")
            ACK((0, "Your device is now deregistered in database"), sock)
        
    except Exception as e:
        if(myLocks.devicesLock._is_owned()):
            myLocks.devicesLock.release()
        print("Deregister in db unsuccessful")
        print(traceback.format_exc())
        NACK((1, str(e)), sock)

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
def MSG(senderId, receiverId, message, sock):
    try:
        print("Adding message from " + senderId + " to " + receiverId)
        myLocks.mailLock.acquire(True)
        dbCursor.execute('SELECT * FROM devices WHERE name = ?', (senderId, ))
        result = dbCursor.fetchall()
        if len(result) == 0:
            myLocks.mailLock.release()
            NACK((1, "Your ID is not registered in database"), sock)
            return
            
        dbCursor.execute('SELECT * FROM devices WHERE name = ?', (receiverId, ))
        result = dbCursor.fetchall()
        if len(result) == 0:
            myLocks.mailLock.release()
            NACK((1, "Receiver Id is not registered in database"), sock)
            return
        
        dbCursor.execute('INSERT INTO mailbox(toId, fromId, message, timestamp) VALUES(?, ?, ?, datetime("now"))',
                          (receiverId, senderId, message) )
        sqlConnection.commit()
        myLocks.mailLock.release()
        ACK((0, "Message was saved in the database"), sock)
        
    except:
        if(myLocks.mailLock._is_owned()):
            myLocks.mailLock.release()
        print("Message saved unsuccessfully")
        print(traceback.format_exc())
        NACK((1, "Error occurred while saving message"), sock)
        
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
def QUERY(qType, deviceId, sock):
    if qType is 0:
        try:
            print("Querying mailbox for " + deviceId)
            myLocks.mailLock.acquire(True)
            dbCursor.execute('SELECT * FROM mailbox WHERE toId = ? ORDER BY id DESC', (deviceId, ))
            result = dbCursor.fetchall()
            myLocks.mailLock.release()
            ACK((0, "Here is your mail", result), sock)
        except:
            if(myLocks.mailLock._is_owned()):
                myLocks.mailLock.release()
            print("Query unsuccessful")
            print(traceback.format_exc())
            NACK((1, "Error occurred while querying your mail"), sock) 
    elif qType is 1:
        try:
            print("Querying server for " + deviceId)
            myLocks.devicesLock.acquire(True)
            dbCursor.execute('SELECT * FROM devices WHERE name = ?', (deviceId, ))
            result = dbCursor.fetchall()
            myLocks.devicesLock.release()
            if len(result) == 0:
                result = None
                ACK((0, "Device is not currently registered", result), sock)
            else:
                ACK((0, "Device is registered currently", result), sock)
        except:
            if(myLocks.devicesLock._is_owned()):
                myLocks.devicesLock.release()
            print("Query unsuccessful")
            print(traceback.format_exc())
            NACK((1, "Error occurred while querying your mail"), sock) 

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
def ACK(response, sock):
    response = str.encode(str(response))
    print("Sending ACK")
    sock.send(response)        

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
def NACK(response, sock):
    response = str.encode(str(response))
    print("Sending NACK")
    sock.send(response)     
    
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
sqlConnection = sqlite3.connect('Proxy_Data.db', check_same_thread=False)
dbCursor = sqlConnection.cursor()
dbCursor.execute('CREATE TABLE IF NOT EXISTS devices (id INTEGER PRIMARY KEY, name TEXT, macAddress TEXT, IP TEXT, portNum TEXT)')
dbCursor.execute('CREATE TABLE IF NOT EXISTS mailbox (id INTEGER PRIMARY KEY, toId TEXT, fromId TEXT, message TEXT, timestamp TEXT)')
print("Db connected")

#Create Class object containing necessary data locks
myLocks = sharedDataLocks()
threadList = []
threadNum = -1
    
#Socket Setup Code
TCPsocket = socket(AF_INET, SOCK_STREAM)
myIP = "192.168.5.5"
myPortNumber = 9999
TCPsocket.bind((myIP, myPortNumber))
TCPsocket.listen(5)
print ("Socket Created")


#Server will always be open while program is ran to receive requests from
#a potential client
ServerOn = True
while ServerOn is True:
    print("Waiting for connection" + "\n")
    clientConnect, addr = TCPsocket.accept()
    threadNum = threadNum + 1
    threadList.append(clientThread(threadNum, clientConnect, addr ))
    threadList[threadNum].start()

