# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 905)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 781, 521, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 781, 541, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.inpMonthIncome = QtWidgets.QLineEdit(self.centralwidget)
        self.inpMonthIncome.setGeometry(QtCore.QRect(670, 80, 113, 32))
        self.inpMonthIncome.setText("")
        self.inpMonthIncome.setObjectName("inpMonthIncome")
        self.inpWage = QtWidgets.QLineEdit(self.centralwidget)
        self.inpWage.setGeometry(QtCore.QRect(670, 120, 113, 32))
        self.inpWage.setText("")
        self.inpWage.setObjectName("inpWage")
        self.inpParrentWage = QtWidgets.QLineEdit(self.centralwidget)
        self.inpParrentWage.setGeometry(QtCore.QRect(670, 160, 113, 32))
        self.inpParrentWage.setText("")
        self.inpParrentWage.setObjectName("inpParrentWage")
        self.inpRent = QtWidgets.QLineEdit(self.centralwidget)
        self.inpRent.setGeometry(QtCore.QRect(670, 200, 113, 32))
        self.inpRent.setText("")
        self.inpRent.setObjectName("inpRent")
        self.inpAllowance = QtWidgets.QLineEdit(self.centralwidget)
        self.inpAllowance.setGeometry(QtCore.QRect(670, 240, 113, 32))
        self.inpAllowance.setText("")
        self.inpAllowance.setObjectName("inpAllowance")
        self.inpSaving = QtWidgets.QLineEdit(self.centralwidget)
        self.inpSaving.setGeometry(QtCore.QRect(670, 320, 113, 32))
        self.inpSaving.setText("")
        self.inpSaving.setObjectName("inpSaving")
        self.inpCashback = QtWidgets.QLineEdit(self.centralwidget)
        self.inpCashback.setGeometry(QtCore.QRect(670, 280, 113, 32))
        self.inpCashback.setText("")
        self.inpCashback.setObjectName("inpCashback")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Сбросить"))
        self.pushButton_2.setText(_translate("MainWindow", "Рассчитать"))

