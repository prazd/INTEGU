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
        MainWindow.resize(1235, 905)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(0, 780, 611, 71))
        self.clear.setObjectName("clear")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(610, 780, 621, 71))
        self.run.setObjectName("run")
        self.inpWage = QtWidgets.QLineEdit(self.centralwidget)
        self.inpWage.setGeometry(QtCore.QRect(290, 180, 113, 32))
        self.inpWage.setText("")
        self.inpWage.setObjectName("inpWage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 140, 331, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 190, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 240, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 300, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 350, 281, 61))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 440, 121, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 500, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 580, 161, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(690, 140, 331, 20))
        self.label_9.setObjectName("label_9")
        self.inpParrentWage = QtWidgets.QLineEdit(self.centralwidget)
        self.inpParrentWage.setGeometry(QtCore.QRect(290, 240, 113, 32))
        self.inpParrentWage.setText("")
        self.inpParrentWage.setObjectName("inpParrentWage")
        self.inpRent = QtWidgets.QLineEdit(self.centralwidget)
        self.inpRent.setGeometry(QtCore.QRect(290, 290, 113, 32))
        self.inpRent.setText("")
        self.inpRent.setObjectName("inpRent")
        self.inpAllowance = QtWidgets.QLineEdit(self.centralwidget)
        self.inpAllowance.setGeometry(QtCore.QRect(340, 360, 113, 32))
        self.inpAllowance.setText("")
        self.inpAllowance.setObjectName("inpAllowance")
        self.inpCashback = QtWidgets.QLineEdit(self.centralwidget)
        self.inpCashback.setGeometry(QtCore.QRect(260, 430, 113, 32))
        self.inpCashback.setText("")
        self.inpCashback.setObjectName("inpCashback")
        self.inpSaving = QtWidgets.QLineEdit(self.centralwidget)
        self.inpSaving.setGeometry(QtCore.QRect(240, 490, 113, 32))
        self.inpSaving.setText("")
        self.inpSaving.setObjectName("inpSaving")
        self.anotherIncome = QtWidgets.QLineEdit(self.centralwidget)
        self.anotherIncome.setGeometry(QtCore.QRect(250, 570, 113, 32))
        self.anotherIncome.setText("")
        self.anotherIncome.setObjectName("anotherIncome")
        self.utilities = QtWidgets.QLineEdit(self.centralwidget)
        self.utilities.setGeometry(QtCore.QRect(840, 170, 113, 32))
        self.utilities.setText("")
        self.utilities.setObjectName("utilities")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(690, 180, 161, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(690, 230, 121, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(690, 310, 121, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(690, 270, 121, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(690, 350, 121, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(690, 400, 121, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(690, 440, 121, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(690, 480, 221, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(680, 590, 221, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(680, 540, 131, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(680, 630, 221, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(660, 720, 221, 20))
        self.label_21.setObjectName("label_21")
        self.rentalOfProperty = QtWidgets.QLineEdit(self.centralwidget)
        self.rentalOfProperty.setGeometry(QtCore.QRect(800, 220, 113, 32))
        self.rentalOfProperty.setText("")
        self.rentalOfProperty.setObjectName("rentalOfProperty")
        self.loanRepayment = QtWidgets.QLineEdit(self.centralwidget)
        self.loanRepayment.setGeometry(QtCore.QRect(840, 260, 113, 32))
        self.loanRepayment.setText("")
        self.loanRepayment.setObjectName("loanRepayment")
        self.education = QtWidgets.QLineEdit(self.centralwidget)
        self.education.setGeometry(QtCore.QRect(790, 300, 113, 32))
        self.education.setText("")
        self.education.setObjectName("education")
        self.healthCare = QtWidgets.QLineEdit(self.centralwidget)
        self.healthCare.setGeometry(QtCore.QRect(820, 340, 113, 32))
        self.healthCare.setText("")
        self.healthCare.setObjectName("healthCare")
        self.nutrion = QtWidgets.QLineEdit(self.centralwidget)
        self.nutrion.setGeometry(QtCore.QRect(790, 390, 113, 32))
        self.nutrion.setText("")
        self.nutrion.setObjectName("nutrion")
        self.clothing = QtWidgets.QLineEdit(self.centralwidget)
        self.clothing.setGeometry(QtCore.QRect(780, 430, 113, 32))
        self.clothing.setText("")
        self.clothing.setObjectName("clothing")
        self.housewares = QtWidgets.QLineEdit(self.centralwidget)
        self.housewares.setGeometry(QtCore.QRect(910, 480, 113, 32))
        self.housewares.setText("")
        self.housewares.setObjectName("housewares")
        self.phoneOrInternet = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneOrInternet.setGeometry(QtCore.QRect(820, 530, 113, 32))
        self.phoneOrInternet.setText("")
        self.phoneOrInternet.setObjectName("phoneOrInternet")
        self.directions = QtWidgets.QLineEdit(self.centralwidget)
        self.directions.setGeometry(QtCore.QRect(740, 580, 113, 32))
        self.directions.setText("")
        self.directions.setObjectName("directions")
        self.fines = QtWidgets.QLineEdit(self.centralwidget)
        self.fines.setGeometry(QtCore.QRect(750, 620, 113, 32))
        self.fines.setText("")
        self.fines.setObjectName("fines")
        self.fun = QtWidgets.QLineEdit(self.centralwidget)
        self.fun.setGeometry(QtCore.QRect(760, 660, 113, 32))
        self.fun.setText("")
        self.fun.setObjectName("fun")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(410, 190, 31, 20))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(410, 250, 31, 20))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(460, 370, 31, 20))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(410, 300, 31, 20))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(390, 440, 31, 20))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(370, 500, 31, 20))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(370, 580, 31, 20))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(970, 170, 31, 20))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(920, 230, 31, 20))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(960, 270, 31, 20))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(910, 310, 31, 20))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(940, 350, 31, 20))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(910, 400, 31, 20))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(900, 430, 31, 20))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(940, 540, 31, 20))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(1030, 490, 31, 20))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(870, 630, 31, 20))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(890, 720, 31, 20))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(860, 580, 31, 20))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(660, 670, 101, 20))
        self.label_41.setObjectName("label_41")
        self.otherExpenses = QtWidgets.QLineEdit(self.centralwidget)
        self.otherExpenses.setGeometry(QtCore.QRect(760, 710, 113, 32))
        self.otherExpenses.setText("")
        self.otherExpenses.setObjectName("otherExpenses")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(880, 670, 31, 20))
        self.label_42.setObjectName("label_42")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1235, 26))
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
        self.clear.setText(_translate("MainWindow", "Сбросить"))
        self.run.setText(_translate("MainWindow", "Рассчитать"))
        self.label.setText(_translate("MainWindow", "- Ваш ежемесячный доход:"))
        self.label_2.setText(_translate("MainWindow", "Заработная плата"))
        self.label_3.setText(_translate("MainWindow", "ЗП родителей"))
        self.label_4.setText(_translate("MainWindow", "Доход от аренды"))
        self.label_5.setText(_translate("MainWindow", "Пособие или иная социальная выплата"))
        self.label_6.setText(_translate("MainWindow", "Пассивный доход"))
        self.label_7.setText(_translate("MainWindow", "Сбережения"))
        self.label_8.setText(_translate("MainWindow", "Иной источник дохода"))
        self.label_9.setText(_translate("MainWindow", "- Ваш ежемесячный расход:"))
        self.label_10.setText(_translate("MainWindow", "Коммунальные услуги"))
        self.label_11.setText(_translate("MainWindow", "Аренда жилья"))
        self.label_12.setText(_translate("MainWindow", "Образование"))
        self.label_13.setText(_translate("MainWindow", "Погашение кредита"))
        self.label_14.setText(_translate("MainWindow", "Здравоохранение"))
        self.label_15.setText(_translate("MainWindow", "Питание"))
        self.label_16.setText(_translate("MainWindow", "Одежда"))
        self.label_17.setText(_translate("MainWindow", "Предметы домашнего обихода"))
        self.label_18.setText(_translate("MainWindow", "Проезд"))
        self.label_19.setText(_translate("MainWindow", "Интернет, телефон"))
        self.label_20.setText(_translate("MainWindow", "Штрафы"))
        self.label_21.setText(_translate("MainWindow", "Иные расходы"))
        self.label_22.setText(_translate("MainWindow", "руб."))
        self.label_23.setText(_translate("MainWindow", "руб."))
        self.label_24.setText(_translate("MainWindow", "руб."))
        self.label_25.setText(_translate("MainWindow", "руб."))
        self.label_26.setText(_translate("MainWindow", "руб."))
        self.label_27.setText(_translate("MainWindow", "руб."))
        self.label_28.setText(_translate("MainWindow", "руб."))
        self.label_29.setText(_translate("MainWindow", "руб."))
        self.label_30.setText(_translate("MainWindow", "руб."))
        self.label_31.setText(_translate("MainWindow", "руб."))
        self.label_32.setText(_translate("MainWindow", "руб."))
        self.label_33.setText(_translate("MainWindow", "руб."))
        self.label_34.setText(_translate("MainWindow", "руб."))
        self.label_35.setText(_translate("MainWindow", "руб."))
        self.label_36.setText(_translate("MainWindow", "руб."))
        self.label_37.setText(_translate("MainWindow", "руб."))
        self.label_38.setText(_translate("MainWindow", "руб."))
        self.label_39.setText(_translate("MainWindow", "руб."))
        self.label_40.setText(_translate("MainWindow", "руб."))
        self.label_41.setText(_translate("MainWindow", "Развлечения"))
        self.label_42.setText(_translate("MainWindow", "руб."))
