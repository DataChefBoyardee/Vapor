# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createacc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sign_Up_Dialog(object):
    def setupUi(self, Sign_Up_Dialog):
        Sign_Up_Dialog.setObjectName("Sign_Up_Dialog")
        Sign_Up_Dialog.resize(600, 800)
        Sign_Up_Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.pEdit = QtWidgets.QLineEdit(Sign_Up_Dialog)
        self.pEdit.setGeometry(QtCore.QRect(290, 360, 181, 31))
        self.pEdit.setStyleSheet("color:rgb(255, 255, 255);")
        self.pEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pEdit.setObjectName("pEdit")
        self.label = QtWidgets.QLabel(Sign_Up_Dialog)
        self.label.setGeometry(QtCore.QRect(160, 260, 391, 21))
        self.label.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label.setObjectName("label")
        self.uLabel = QtWidgets.QLabel(Sign_Up_Dialog)
        self.uLabel.setGeometry(QtCore.QRect(150, 310, 121, 21))
        self.uLabel.setStyleSheet("color:rgb(255, 255, 255); font-size:15pt;")
        self.uLabel.setObjectName("uLabel")
        self.greeting = QtWidgets.QLabel(Sign_Up_Dialog)
        self.greeting.setGeometry(QtCore.QRect(200, 180, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(27)
        self.greeting.setFont(font)
        self.greeting.setStyleSheet("color:rgb(255, 255, 255);")
        self.greeting.setAlignment(QtCore.Qt.AlignCenter)
        self.greeting.setWordWrap(False)
        self.greeting.setObjectName("greeting")
        self.pLabel = QtWidgets.QLabel(Sign_Up_Dialog)
        self.pLabel.setGeometry(QtCore.QRect(150, 360, 121, 21))
        self.pLabel.setStyleSheet("color:rgb(255, 255, 255); font-size:15pt;")
        self.pLabel.setObjectName("pLabel")
        self.createAccountButton = QtWidgets.QPushButton(Sign_Up_Dialog)
        self.createAccountButton.setGeometry(QtCore.QRect(200, 510, 201, 41))
        self.createAccountButton.setStyleSheet("color:rgb(255, 255, 255)")
        self.createAccountButton.setObjectName("createAccountButton")
        self.uEdit = QtWidgets.QLineEdit(Sign_Up_Dialog)
        self.uEdit.setGeometry(QtCore.QRect(290, 310, 181, 31))
        self.uEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.uEdit.setObjectName("uEdit")
        self.pLabel_2 = QtWidgets.QLabel(Sign_Up_Dialog)
        self.pLabel_2.setGeometry(QtCore.QRect(80, 410, 201, 21))
        self.pLabel_2.setStyleSheet("color:rgb(255, 255, 255); font-size:15pt;")
        self.pLabel_2.setObjectName("pLabel_2")
        self.pEdit_2 = QtWidgets.QLineEdit(Sign_Up_Dialog)
        self.pEdit_2.setGeometry(QtCore.QRect(290, 410, 181, 31))
        self.pEdit_2.setStyleSheet("color:rgb(255, 255, 255);")
        self.pEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pEdit_2.setObjectName("pEdit_2")
        self.cLabel = QtWidgets.QLabel(Sign_Up_Dialog)
        self.cLabel.setGeometry(QtCore.QRect(50, 460, 201, 21))
        self.cLabel.setStyleSheet("color:rgb(255, 255, 255); font-size:15pt;")
        self.cLabel.setObjectName("cLabel")
        self.cEdit = QtWidgets.QLineEdit(Sign_Up_Dialog)
        self.cEdit.setGeometry(QtCore.QRect(290, 460, 181, 31))
        self.cEdit.setStyleSheet("color:rgb(255, 255, 255);")
        self.cEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.cEdit.setObjectName("cEdit")

        self.retranslateUi(Sign_Up_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Sign_Up_Dialog)

    def retranslateUi(self, Sign_Up_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Sign_Up_Dialog.setWindowTitle(_translate("Sign_Up_Dialog", "Create Account"))
        self.label.setText(_translate("Sign_Up_Dialog", "Please enter your username and password."))
        self.uLabel.setText(_translate("Sign_Up_Dialog", "Username"))
        self.greeting.setText(_translate("Sign_Up_Dialog", "Sign Up"))
        self.pLabel.setText(_translate("Sign_Up_Dialog", "Password"))
        self.createAccountButton.setText(_translate("Sign_Up_Dialog", "Create Account"))
        self.uEdit.setWhatsThis(_translate("Sign_Up_Dialog", "<html><head/><body><p>color:rgb(255, 255, 255);</p></body></html>"))
        self.pLabel_2.setText(_translate("Sign_Up_Dialog", "Confirm Password"))
        self.cLabel.setText(_translate("Sign_Up_Dialog", "Country of Residence"))
