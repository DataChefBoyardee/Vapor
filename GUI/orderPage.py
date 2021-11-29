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
        self.buttonBox = QtWidgets.QDialogButtonBox(orderPage)
        self.buttonBox.setGeometry(QtCore.QRect(150, 420, 181, 32))
        self.buttonBox.setStyleSheet("color: rgb(255, 255, 255)")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(orderPage)
        self.label.setGeometry(QtCore.QRect(170, 40, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(orderPage)
        self.listView.setGeometry(QtCore.QRect(35, 140, 431, 181))
        self.listView.setObjectName("listView")
        self.label_2 = QtWidgets.QLabel(orderPage)
        self.label_2.setGeometry(QtCore.QRect(200, 380, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(orderPage)
        self.buttonBox.accepted.connect(orderPage.accept)
        self.buttonBox.rejected.connect(orderPage.reject)
        QtCore.QMetaObject.connectSlotsByName(orderPage)

    def retranslateUi(self, orderPage):
        _translate = QtCore.QCoreApplication.translate
        orderPage.setWindowTitle(_translate("orderPage", "Order Summary"))
        self.label.setText(_translate("orderPage", "Order Summary:"))
        self.label_2.setText(_translate("orderPage", "Confirm Order"))
