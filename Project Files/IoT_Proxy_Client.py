'''
Created on Dec 4, 2019

@author: Matthew Cook
'''

import sys
from socket import socket
from uuid import getnode
from ast import literal_eval
import traceback
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

########################### PyQt5 UI ###############################################################

# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.13.0

##################### MAIN WINDOW ############################
class Ui_LocalProxyNetwork(object):
    def setupUi(self, LocalProxyNetwork):
        LocalProxyNetwork.setObjectName("LocalProxyNetwork")
        LocalProxyNetwork.resize(837, 659)
        self.centralwidget = QtWidgets.QWidget(LocalProxyNetwork)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(120, 60, 161, 71))
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.clicked.connect(self.registerWindow)
        
        self.btnDeregister = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeregister.setGeometry(QtCore.QRect(120, 280, 161, 71))
        self.btnDeregister.setObjectName("btnDeregister")
        self.btnDeregister.clicked.connect(self.deregisterWindow)
        
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(560, 280, 161, 71))
        self.btnQuery.setObjectName("btnQuery")
        self.btnQuery.clicked.connect(self.queryWindow)
        
        self.btnMessage = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessage.setGeometry(QtCore.QRect(560, 60, 161, 71))
        self.btnMessage.setObjectName("btnMessage")
        self.btnMessage.clicked.connect(self.messageWindow)
        
        self.btnQuit = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuit.setGeometry(QtCore.QRect(330, 180, 161, 71))
        self.btnQuit.setObjectName("btnQuit")
        self.btnQuit.clicked.connect(QUIT)
        
        self.lbCommand = QtWidgets.QLabel(self.centralwidget)
        self.lbCommand.setGeometry(QtCore.QRect(350, 0, 160, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
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
        self.textBrowser.setFont(font)
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
    
    def showPop(self):
        msg = QMessageBox()
        msg.setWindowTitle("Register Stuff")
        msg.setText("Do some register stuff")
        ex = msg.exec_()
    
    def registerWindow(self):
        self.registerWindow = QtWidgets.QMainWindow()
        ui = Ui_RegisterWindow()
        ui.setupUi(self.registerWindow)
        self.registerWindow.show()
    
    def deregisterWindow(self):
        self.deregisterWindow = QtWidgets.QMainWindow()
        ui = Ui_DeregisterWindow()
        ui.setupUi(self.deregisterWindow)
        self.deregisterWindow.show()   
        
    def messageWindow(self):
        self.messageWindow = QtWidgets.QMainWindow()
        ui = Ui_MessageWindow()
        ui.setupUi(self.messageWindow)
        self.messageWindow.show()

    def queryWindow(self):
        self.queryWindow = QtWidgets.QMainWindow()
        ui = Ui_QueryWindow()
        ui.setupUi(self.queryWindow)
        self.queryWindow.show()
        
##################### REGISTER WINDOW ############################

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(491, 262)
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblRegister = QtWidgets.QLabel(self.centralwidget)
        self.lblRegister.setGeometry(QtCore.QRect(10, 50, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblRegister.setFont(font)
        self.lblRegister.setObjectName("lblRegister")
        
        self.editRegister = QtWidgets.QTextEdit(self.centralwidget)
        self.editRegister.setGeometry(QtCore.QRect(310, 40, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editRegister.setFont(font)
        self.editRegister.setObjectName("editRegister")
        
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(170, 140, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRegister.setFont(font)
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.clicked.connect(lambda: self.registerDevice())
        
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        self.lblRegister.setText(_translate("RegisterWindow", "Please Enter a nickname for your device:"))
        self.btnRegister.setText(_translate("RegisterWindow", "Register"))
        
    def registerDevice(self):
        deviceId = self.editRegister.toPlainText()
        REGISTER(deviceId)

##################### DEREGISTER WINDOW ############################

class Ui_DeregisterWindow(object):
    def setupUi(self, DeregisterWindow):
        DeregisterWindow.setObjectName("DeregisterWindow")
        DeregisterWindow.resize(491, 261)
        self.centralwidget = QtWidgets.QWidget(DeregisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblDeregister = QtWidgets.QLabel(self.centralwidget)
        self.lblDeregister.setGeometry(QtCore.QRect(10, 50, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblDeregister.setFont(font)
        self.lblDeregister.setObjectName("lblDeregister")
        
        self.editDeregister = QtWidgets.QTextEdit(self.centralwidget)
        self.editDeregister.setGeometry(QtCore.QRect(320, 40, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editDeregister.setFont(font)
        self.editDeregister.setObjectName("editDeregister")
        
        self.btnDeregister = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeregister.setGeometry(QtCore.QRect(170, 140, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDeregister.setFont(font)
        self.btnDeregister.setObjectName("btnDeregister")
        self.btnDeregister.clicked.connect(lambda: self.deregisterDevice())
        
        DeregisterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DeregisterWindow)
        self.statusbar.setObjectName("statusbar")
        DeregisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DeregisterWindow)
        QtCore.QMetaObject.connectSlotsByName(DeregisterWindow)

    def retranslateUi(self, DeregisterWindow):
        _translate = QtCore.QCoreApplication.translate
        DeregisterWindow.setWindowTitle(_translate("DeregisterWindow", "MainWindow"))
        self.lblDeregister.setText(_translate("DeregisterWindow", "Please enter the nickname for your device:"))
        self.btnDeregister.setText(_translate("DeregisterWindow", "Deregister"))
        
    def deregisterDevice(self):
        deviceId = self.editDeregister.toPlainText()
        DEREGISTER(deviceId)
        
##################### MESSAGE WINDOW ############################

class Ui_MessageWindow(object):
    def setupUi(self, MessageWindow):
        MessageWindow.setObjectName("MessageWindow")
        MessageWindow.resize(487, 380)
        self.centralwidget = QtWidgets.QWidget(MessageWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(170, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        
        self.lblTo = QtWidgets.QLabel(self.centralwidget)
        self.lblTo.setGeometry(QtCore.QRect(110, 50, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTo.setFont(font)
        self.lblTo.setObjectName("lblTo")
        
        self.lblFrom = QtWidgets.QLabel(self.centralwidget)
        self.lblFrom.setGeometry(QtCore.QRect(90, 110, 47, 14))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblFrom.setFont(font)
        self.lblFrom.setObjectName("lblFrom")
        
        self.editTo = QtWidgets.QTextEdit(self.centralwidget)
        self.editTo.setGeometry(QtCore.QRect(140, 50, 161, 31))
        self.editTo.setObjectName("editTo")
        self.editTo.setFont(font)
        
        self.editMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.editMessage.setGeometry(QtCore.QRect(140, 150, 251, 111))
        self.editMessage.setObjectName("editMessage")
        self.editMessage.setFont(font)
        
        self.editFrom = QtWidgets.QTextEdit(self.centralwidget)
        self.editFrom.setGeometry(QtCore.QRect(140, 100, 161, 31))
        self.editFrom.setObjectName("editFrom")
        self.editFrom.setFont(font)
        
        self.lblMessage = QtWidgets.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(70, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage.setFont(font)
        self.lblMessage.setObjectName("lblMessage")
        
        self.btnDeregister = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeregister.setGeometry(QtCore.QRect(200, 280, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDeregister.setFont(font)
        self.btnDeregister.setObjectName("btnDeregister")
        self.btnDeregister.clicked.connect(lambda: self.messageDevice())
        
        MessageWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MessageWindow)
        self.statusbar.setObjectName("statusbar")
        MessageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MessageWindow)
        QtCore.QMetaObject.connectSlotsByName(MessageWindow)

    def retranslateUi(self, MessageWindow):
        _translate = QtCore.QCoreApplication.translate
        MessageWindow.setWindowTitle(_translate("MessageWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MessageWindow", "New Message"))
        self.lblTo.setText(_translate("MessageWindow", "To:"))
        self.lblFrom.setText(_translate("MessageWindow", "From:"))
        self.editMessage.setHtml(_translate("MessageWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lblMessage.setText(_translate("MessageWindow", "Message:"))
        self.btnDeregister.setText(_translate("MessageWindow", "Send"))
        
    def messageDevice(self):
        toId = self.editTo.toPlainText()
        fromId = self.editFrom.toPlainText()
        message = self.editMessage.toPlainText()
        MSG(fromId, toId, message)
        
##################### QUERY WINDOW ############################


class Ui_QueryWindow(object):
    def setupUi(self, QueryWindow):
        QueryWindow.setObjectName("QueryWindow")
        QueryWindow.resize(474, 332)
        self.centralwidget = QtWidgets.QWidget(QueryWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(190, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        
        self.lblDeviceId = QtWidgets.QLabel(self.centralwidget)
        self.lblDeviceId.setGeometry(QtCore.QRect(70, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblDeviceId.setFont(font)
        self.lblDeviceId.setObjectName("lblDeviceId")
        
        self.lblMessage = QtWidgets.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(130, 100, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage.setFont(font)
        self.lblMessage.setObjectName("lblMessage")
        
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(180, 230, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnQuery.setFont(font)
        self.btnQuery.setObjectName("btnQuery")
        self.btnQuery.clicked.connect(lambda: self.queryDevice())
        
        self.editDeviceId = QtWidgets.QTextEdit(self.centralwidget)
        self.editDeviceId.setGeometry(QtCore.QRect(180, 50, 161, 31))
        self.editDeviceId.setObjectName("editDeviceId")
        self.editDeviceId.setFont(font)
        
        self.lblType = QtWidgets.QLabel(self.centralwidget)
        self.lblType.setGeometry(QtCore.QRect(190, 100, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblType.setFont(font)
        self.lblType.setObjectName("lblType")
        
        self.sliderType = QtWidgets.QSlider(self.centralwidget)
        self.sliderType.setGeometry(QtCore.QRect(120, 160, 241, 21))
        self.sliderType.setMaximum(1)
        self.sliderType.setOrientation(QtCore.Qt.Horizontal)
        self.sliderType.setObjectName("sliderType")
        self.sliderType.valueChanged.connect(lambda: self.adjustTypeLabel())
        
        QueryWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QueryWindow)
        self.statusbar.setObjectName("statusbar")
        QueryWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QueryWindow)
        QtCore.QMetaObject.connectSlotsByName(QueryWindow)

    def retranslateUi(self, QueryWindow):
        _translate = QtCore.QCoreApplication.translate
        QueryWindow.setWindowTitle(_translate("QueryWindow", "MainWindow"))
        self.lblTitle.setText(_translate("QueryWindow", "Data Query"))
        self.lblDeviceId.setText(_translate("QueryWindow", "Target Device:"))
        self.lblMessage.setText(_translate("QueryWindow", "Type:"))
        self.btnQuery.setText(_translate("QueryWindow", "Send"))
        self.lblType.setText(_translate("QueryWindow", "Mailbox"))
        
    def adjustTypeLabel(self):
        numType = self.sliderType.value()
        if(numType is 0):
            self.lblType.setText("Mailbox")
        elif(numType is 1):
            self.lblType.setText("Device Information")
            
    def queryDevice(self):
        numType = self.sliderType.value()
        targetDevice = self.editDeviceId.toPlainText()
        QUERY(numType, targetDevice)
        
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
        print("ACK: " + recvData[1] + '\n')
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n" + '\n')
    elif recvData[0] is 1: #Received message is a NACK
        print("NACK: " + recvData[1] + '\n')
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "NACK: " + recvData[1] + "\n" + '\n')


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
        print("ACK: " + recvData[1] + '\n')
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n" + '\n')
    elif recvData[0] is 1: #Received message is a NACK
        print("NACK: " + recvData[1] + '\n')
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "NACK: " + recvData[1] + "\n" + '\n')

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
def MSG(fromId, toID, message):
    myMessage = (3, fromId, toID, message)
    myMessage = str.encode(str(myMessage))
    socketTCP.send(myMessage)
    recvData = socketTCP.recv(1024)
    recvData = bytes.decode(recvData)
    recvData = literal_eval(recvData)
    if recvData[0] is 0: #Received message is a ACK
        print("ACK: " + recvData[1] + '\n')
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "ACK: " + recvData[1] + "\n" + '\n')
    elif recvData[0] is 1:#Received message is a NACK
        print("NACK: " + recvData[1] + '\n')
        ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "NACK: " + recvData[1] + "\n" + '\n')
      
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
    try:
        if qType is 0:
            print("Mailbox Query")
            ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "Mailbox Query" + "\n")
            myMessage = (4, 0, deviceId)
            myMessage = str.encode(str(myMessage))
            socketTCP.send(myMessage)
            recvData = socketTCP.recv(2048)
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
    except Exception as e:
            print(traceback.format_exc())
        
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
    sys.exit(app.exec_())


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
    print("\n")
    ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "\n")         
            
            

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
    print("\n")
    ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + "\n")    

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
#userId = "Kamran's Tower"
#userId2 = "Nope"

#Client Functions Testing
#REGISTER(userId) 
#REGISTER(userId2)
#MSG(userId, userId2, "Testing test")
#QUERY(0, userId2)
#QUERY(1, userId2)
