'''
Created on Dec 4, 2019

@author: Matthew Cook
'''

import sys
from socket import socket
from uuid import getnode
from ast import literal_eval
from PyQt5 import QtCore, QtGui, QtWidgets

########################### PyQt5 UI ###############################################################

# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.13.0


class Ui_LocalProxyNetwork(object):
    def setupUi(self, LocalProxyNetwork):
        LocalProxyNetwork.setObjectName("LocalProxyNetwork")
        LocalProxyNetwork.resize(837, 659)
        self.centralwidget = QtWidgets.QWidget(LocalProxyNetwork)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(120, 60, 161, 71))
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.clicked.connect(lambda: REGISTER("Kamran's Tower"))
        
        self.btnDeregister = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeregister.setGeometry(QtCore.QRect(120, 280, 161, 71))
        self.btnDeregister.setObjectName("btnDeregister")
        self.btnDeregister.clicked.connect(lambda: DEREGISTER("Kamran's Tower"))
        
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(560, 280, 161, 71))
        self.btnQuery.setObjectName("btnQuery")
        self.btnQuery.clicked.connect(lambda: QUERY(0, "Nope"))
        
        self.btnMessage = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessage.setGeometry(QtCore.QRect(560, 60, 161, 71))
        self.btnMessage.setObjectName("btnMessage")
        self.btnMessage.clicked.connect(lambda: MSG("Kamran's Tower", "Nope", "Testing test"))
        
        self.btnQuit = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuit.setGeometry(QtCore.QRect(330, 180, 161, 71))
        self.btnQuit.setObjectName("btnQuit")
        self.btnQuit.clicked.connect(QUIT)
        
        self.lbCommand = QtWidgets.QLabel(self.centralwidget)
        self.lbCommand.setGeometry(QtCore.QRect(350, 0, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbCommand.setFont(font)
        self.lbCommand.setObjectName("lbCommand")
        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 380, 741, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 249))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lbOutput = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbOutput.setGeometry(QtCore.QRect(300, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbOutput.setFont(font)
        self.lbOutput.setObjectName("lbOutput")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 721, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        LocalProxyNetwork.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LocalProxyNetwork)
        self.statusbar.setObjectName("statusbar")
        LocalProxyNetwork.setStatusBar(self.statusbar)

        self.retranslateUi(LocalProxyNetwork)
        QtCore.QMetaObject.connectSlotsByName(LocalProxyNetwork)

    def retranslateUi(self, LocalProxyNetwork):
        _translate = QtCore.QCoreApplication.translate
        LocalProxyNetwork.setWindowTitle(_translate("LocalProxyNetwork", "MainWindow"))
        self.btnRegister.setText(_translate("LocalProxyNetwork", "REGISTER"))
        self.btnDeregister.setText(_translate("LocalProxyNetwork", "DEREGISTER"))
        self.btnQuery.setText(_translate("LocalProxyNetwork", "QUERY"))
        self.btnMessage.setText(_translate("LocalProxyNetwork", "MESSAGE"))
        self.btnQuit.setText(_translate("LocalProxyNetwork", "QUIT"))
        self.lbCommand.setText(_translate("LocalProxyNetwork", "Commands:"))
        self.lbOutput.setText(_translate("LocalProxyNetwork", "Console Output"))
        self.textBrowser.setHtml(_translate("LocalProxyNetwork", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to Local Proxy Network UI version 1.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Output is below:</p></body></html>"))

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
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n")
    elif recvData[0] is 1: #Received message is a NACK
        print("NACK: " + recvData[1])
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "NACK: " + recvData[1] + "\n")


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
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n")
    elif recvData[0] is 1: #Received message is a NACK
        print("NACK: " + recvData[1])
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "NACK: " + recvData[1] + "\n")

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
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n")
    elif recvData[0] is 1:#Received message is a NACK
        print("NACK: " + recvData[1])
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "NACK: " + recvData[1] + "\n")
      
#Name: QUERY
#
#Purpose: Query database for desired information
#
#Param: in: integer representing type of query (qType)
#       in: string representing device's Id (deviceId)
#
#Brief: Query database for desired information requested by 
#       the client
#
#ErrorsHandled: 
#  
def QUERY(qType, deviceId):
    if qType is 0:
        print("Mailbox Query")
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "Mailbox Query" + "\n")
        myMessage = (4, 0, deviceId)
        myMessage = str.encode(str(myMessage))
        socketTCP.send(myMessage)
        recvData = socketTCP.recv(1024)
        recvData = bytes.decode(recvData)
        recvData = literal_eval(recvData)
        
        if recvData[0] is 0: #Received message is a ACK
            print("ACK: " + recvData[1])
            ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n")
            printMailQuery(recvData[2])
    
        elif recvData[0] is 1:#Received message is a NACK
            print("NACK: " + recvData[1]) 
            ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "NACK: " + recvData[1] + "\n")
    elif qType is 1:
        print("Device Info Query")
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "Device Info Query" + "\n")
        myMessage = (4, 1, deviceId)
        myMessage = str.encode(str(myMessage))
        socketTCP.send(myMessage)
        recvData = socketTCP.recv(1024)
        recvData = bytes.decode(recvData)
        recvData = literal_eval(recvData)
        
        if recvData[0] is 0: #Received message is a ACK
            print("ACK: " + recvData[1])
            ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n")
            printDevicesQuery(recvData[2])
    
        elif recvData[0] is 1:#Received message is a NACK
            print("NACK: " + recvData[1]) 
            ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n")
    else:
        print("Inputted type is not a valid query type")
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "Inputted type is not a valid query type" + "\n")
        
#Name: Quit Application
#
#Purpose: Closes socket connection with network
#
#Param: N/A
#
#Brief: N/A
#
#ErrorsHandled: N/A
#       
def QUIT():
    print("Quitting proxy network and closing socket connection")
    ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "Quitting proxy network and closing socket connection" + "\n")
    socketTCP.close()


#Name: Print Mail Query
#
#Purpose: Prints the result of a database query for mail
#
#Param: in: 2-D Array representing database query (result)
#
#Brief: N/A
#
#ErrorsHandled: N/A
#  
def printMailQuery(result):
    if result is not None:
        for row in result:
            myRow = "To: " + row[1] + "   " + "From: " + row[2] + "    Message: " + row[3] + "   " + "Date: " + row[4]
            print(myRow)
            ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + myRow + "\n")
            
            
            

#Name: Print Devices Query
#
#Purpose: Prints the result of a database query for devices
#
#Param: in: 2-D Array representing database query (result)
#
#Brief: N/A
#
#ErrorsHandled: N/A
#  
def printDevicesQuery(result):
    if result is not None:
        for row in result:
            myRow = "DeviceId: " + row[1] + "   " + "MAC: " + row[2] + "   IP: " + row[3] + "   " + "Port: " + row[4]
            print(myRow)
            ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + myRow + "\n")

####################### MAIN PROGRAM #######################################################################

#Code for client to connect to server
socketTCP = socket()
myIP = "192.168.5.5"
myPortNumber = 9999
socketTCP.connect((myIP, myPortNumber))

#Create PyQt5 Window
app = QtWidgets.QApplication(sys.argv)
LocalProxyNetwork = QtWidgets.QMainWindow()
ui = Ui_LocalProxyNetwork()
ui.setupUi(LocalProxyNetwork)
LocalProxyNetwork.show()
ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "\n\n")
sys.exit(app.exec_())

#Client Information
userId = "Kamran's Tower"
userId2 = "Nope"

#Client Functions Testing
REGISTER(userId) 
REGISTER(userId2)
MSG(userId, userId2, "Testing test")
QUERY(0, userId2)
QUERY(1, userId2)
