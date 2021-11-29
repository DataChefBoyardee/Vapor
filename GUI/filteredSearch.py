# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filteredSearch.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_filteredResults(object):
    def setupUi(self, filteredResults):
        filteredResults.setObjectName("filteredResults")
        filteredResults.resize(1100, 800)
        filteredResults.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.tableFilteredResults = QtWidgets.QTableView(filteredResults)
        self.tableFilteredResults.setGeometry(QtCore.QRect(30, 140, 741, 631))
        self.tableFilteredResults.setStyleSheet("color: rgb(0, 0, 0); background: rgb(189, 189, 189)")
        self.tableFilteredResults.setObjectName("tableFilteredResults")
        self.labelFiltered = QtWidgets.QLabel(filteredResults)
        self.labelFiltered.setGeometry(QtCore.QRect(220, 30, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFiltered.setFont(font)
        self.labelFiltered.setStyleSheet("color: rgb(255, 255, 255)")
        self.labelFiltered.setObjectName("labelFiltered")
        self.filterType = QtWidgets.QLabel(filteredResults)
        self.filterType.setGeometry(QtCore.QRect(370, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filterType.setFont(font)
        self.filterType.setStyleSheet("color: rgb(255, 255, 255)")
        self.filterType.setObjectName("filterType")
        self.score = QtWidgets.QPushButton(filteredResults)
        self.score.setGeometry(QtCore.QRect(790, 280, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.score.setFont(font)
        self.score.setStyleSheet("color: rgb(255, 255, 255)")
        self.score.setObjectName("score")
        self.specials = QtWidgets.QPushButton(filteredResults)
        self.specials.setGeometry(QtCore.QRect(790, 150, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.specials.setFont(font)
        self.specials.setAutoFillBackground(False)
        self.specials.setStyleSheet("color: rgb(255, 255, 255)")
        self.specials.setObjectName("specials")
        self.valveFilter = QtWidgets.QPushButton(filteredResults)
        self.valveFilter.setGeometry(QtCore.QRect(790, 410, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valveFilter.setFont(font)
        self.valveFilter.setStyleSheet("color: rgb(255, 255, 255)")
        self.valveFilter.setObjectName("valveFilter")
        self.orderEdit = QtWidgets.QLineEdit(filteredResults)
        self.orderEdit.setGeometry(QtCore.QRect(60, 90, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orderEdit.setFont(font)
        self.orderEdit.setStyleSheet("color: rgb(255, 255, 255)")
        self.orderEdit.setObjectName("orderEdit")
        self.orderButton = QtWidgets.QPushButton(filteredResults)
        self.orderButton.setGeometry(QtCore.QRect(280, 80, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orderButton.setFont(font)
        self.orderButton.setStyleSheet("color: rgb(255, 255, 255)")
        self.orderButton.setObjectName("orderButton")

        self.retranslateUi(filteredResults)
        QtCore.QMetaObject.connectSlotsByName(filteredResults)

    def retranslateUi(self, filteredResults):
        _translate = QtCore.QCoreApplication.translate
        filteredResults.setWindowTitle(_translate("filteredResults", "Filter Search"))
        self.labelFiltered.setText(_translate("filteredResults", "Filtered Results for: "))
        self.filterType.setText(_translate("filteredResults", "[Insert filter button]"))
        self.score.setText(_translate("filteredResults", "Top Score"))
        self.specials.setText(_translate("filteredResults", "Specials"))
        self.valveFilter.setText(_translate("filteredResults", "Games by Valve"))
        self.orderEdit.setPlaceholderText(_translate("filteredResults", "Enter Game Here"))
        self.orderButton.setText(_translate("filteredResults", "Order"))
