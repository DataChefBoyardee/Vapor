# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_orderPage(object):
    def setupUi(self, orderPage):
        orderPage.setObjectName("orderPage")
        orderPage.resize(500, 500)
        font = QtGui.QFont()
        font.setPointSize(12)
        orderPage.setFont(font)
        orderPage.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.summaryLabel = QtWidgets.QLabel(orderPage)
        self.summaryLabel.setGeometry(QtCore.QRect(170, 40, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.summaryLabel.setFont(font)
        self.summaryLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.summaryLabel.setObjectName("summaryLabel")
        self.confirmLabel = QtWidgets.QLabel(orderPage)
        self.confirmLabel.setGeometry(QtCore.QRect(190, 380, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirmLabel.setFont(font)
        self.confirmLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.confirmLabel.setObjectName("confirmLabel")
        self.Ok = QtWidgets.QPushButton(orderPage)
        self.Ok.setGeometry(QtCore.QRect(140, 430, 100, 40))
        self.Ok.setStyleSheet("color: rgb(255, 255, 255)")
        self.Ok.setObjectName("Ok")
        self.Cancel = QtWidgets.QPushButton(orderPage)
        self.Cancel.setGeometry(QtCore.QRect(260, 430, 100, 40))
        self.Cancel.setStyleSheet("color: rgb(255, 255, 255)")
        self.Cancel.setObjectName("Cancel")
        self.gameLabel = QtWidgets.QLabel(orderPage)
        self.gameLabel.setGeometry(QtCore.QRect(110, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gameLabel.setFont(font)
        self.gameLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.gameLabel.setObjectName("gameLabel")
        self.developerLabel = QtWidgets.QLabel(orderPage)
        self.developerLabel.setGeometry(QtCore.QRect(80, 210, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.developerLabel.setFont(font)
        self.developerLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.developerLabel.setObjectName("developerLabel")
        self.publisherLabel = QtWidgets.QLabel(orderPage)
        self.publisherLabel.setGeometry(QtCore.QRect(90, 260, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.publisherLabel.setFont(font)
        self.publisherLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.publisherLabel.setObjectName("publisherLabel")
        self.priceLabel = QtWidgets.QLabel(orderPage)
        self.priceLabel.setGeometry(QtCore.QRect(120, 310, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.priceLabel.setFont(font)
        self.priceLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.priceLabel.setObjectName("priceLabel")
        self.gameInsertLabel = QtWidgets.QLabel(orderPage)
        self.gameInsertLabel.setGeometry(QtCore.QRect(210, 160, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gameInsertLabel.setFont(font)
        self.gameInsertLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.gameInsertLabel.setObjectName("gameInsertLabel")
        self.developerInsertLabel = QtWidgets.QLabel(orderPage)
        self.developerInsertLabel.setGeometry(QtCore.QRect(210, 210, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.developerInsertLabel.setFont(font)
        self.developerInsertLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.developerInsertLabel.setObjectName("developerInsertLabel")
        self.publisherInsertLabel = QtWidgets.QLabel(orderPage)
        self.publisherInsertLabel.setGeometry(QtCore.QRect(210, 260, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.publisherInsertLabel.setFont(font)
        self.publisherInsertLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.publisherInsertLabel.setObjectName("publisherInsertLabel")
        self.priceInsertLabel = QtWidgets.QLabel(orderPage)
        self.priceInsertLabel.setGeometry(QtCore.QRect(210, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.priceInsertLabel.setFont(font)
        self.priceInsertLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.priceInsertLabel.setObjectName("priceInsertLabel")

        self.retranslateUi(orderPage)
        QtCore.QMetaObject.connectSlotsByName(orderPage)

    def retranslateUi(self, orderPage):
        _translate = QtCore.QCoreApplication.translate
        orderPage.setWindowTitle(_translate("orderPage", "Order Summary"))
        self.summaryLabel.setText(_translate("orderPage", "Order Summary"))
        self.confirmLabel.setText(_translate("orderPage", "Confirm Order?"))
        self.Ok.setText(_translate("orderPage", "Ok"))
        self.Cancel.setText(_translate("orderPage", "Cancel"))
        self.gameLabel.setText(_translate("orderPage", "Game:"))
        self.developerLabel.setText(_translate("orderPage", "Developer:"))
        self.publisherLabel.setText(_translate("orderPage", "Publisher:"))
        self.priceLabel.setText(_translate("orderPage", "Price:"))
        self.gameInsertLabel.setText(_translate("orderPage", "[Insert Game]"))
        self.developerInsertLabel.setText(_translate("orderPage", "[Insert Developer]"))
        self.publisherInsertLabel.setText(_translate("orderPage", "[Insert Publisher]"))
        self.priceInsertLabel.setText(_translate("orderPage", "[Insert Price]"))
