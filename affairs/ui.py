# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affairs.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Affairs(object):
    def setupUi(self, Affairs):
        Affairs.setObjectName("Affairs")
        Affairs.resize(1550, 923)
        self.centralwidget = QtWidgets.QWidget(Affairs)
        self.centralwidget.setObjectName("centralwidget")
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(710, 550, 161, 71))
        self.Run.setObjectName("Run")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 10, 741, 141))
        self.label.setObjectName("label")
        self.affair = QtWidgets.QLineEdit(self.centralwidget)
        self.affair.setGeometry(QtCore.QRect(210, 230, 191, 41))
        self.affair.setText("")
        self.affair.setObjectName("affair")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(1150, 260, 131, 51))
        self.add.setObjectName("add")
        self.impWidget = QtWidgets.QWidget(self.centralwidget)
        self.impWidget.setGeometry(QtCore.QRect(590, 200, 101, 80))
        self.impWidget.setObjectName("impWidget")
        self.fNo = QtWidgets.QRadioButton(self.impWidget)
        self.fNo.setGeometry(QtCore.QRect(60, 20, 21, 25))
        self.fNo.setText("")
        self.fNo.setObjectName("fNo")
        self.label_6 = QtWidgets.QLabel(self.impWidget)
        self.label_6.setGeometry(QtCore.QRect(20, 0, 62, 20))
        self.label_6.setObjectName("label_6")
        self.fYes = QtWidgets.QRadioButton(self.impWidget)
        self.fYes.setGeometry(QtCore.QRect(10, 20, 21, 25))
        self.fYes.setText("")
        self.fYes.setObjectName("fYes")
        self.label_2 = QtWidgets.QLabel(self.impWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 21, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.impWidget)
        self.label_3.setGeometry(QtCore.QRect(60, 50, 31, 20))
        self.label_3.setObjectName("label_3")
        self.urgWidget = QtWidgets.QWidget(self.centralwidget)
        self.urgWidget.setGeometry(QtCore.QRect(910, 200, 120, 80))
        self.urgWidget.setObjectName("urgWidget")
        self.label_7 = QtWidgets.QLabel(self.urgWidget)
        self.label_7.setGeometry(QtCore.QRect(30, 0, 62, 20))
        self.label_7.setObjectName("label_7")
        self.sYes = QtWidgets.QRadioButton(self.urgWidget)
        self.sYes.setGeometry(QtCore.QRect(20, 20, 21, 25))
        self.sYes.setText("")
        self.sYes.setObjectName("sYes")
        self.label_4 = QtWidgets.QLabel(self.urgWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 21, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.urgWidget)
        self.label_5.setGeometry(QtCore.QRect(70, 50, 31, 20))
        self.label_5.setObjectName("label_5")
        self.sNo = QtWidgets.QRadioButton(self.urgWidget)
        self.sNo.setGeometry(QtCore.QRect(70, 20, 21, 25))
        self.sNo.setText("")
        self.sNo.setObjectName("sNo")
        self.fListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.fListWidget.setGeometry(QtCore.QRect(440, 410, 241, 111))
        self.fListWidget.setObjectName("fListWidget")
        self.tListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.tListWidget.setGeometry(QtCore.QRect(500, 770, 241, 111))
        self.tListWidget.setObjectName("tListWidget")
        self.sListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.sListWidget.setGeometry(QtCore.QRect(910, 410, 231, 111))
        self.sListWidget.setObjectName("sListWidget")
        self.lListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.lListWidget.setGeometry(QtCore.QRect(860, 770, 231, 111))
        self.lListWidget.setObjectName("lListWidget")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(710, 660, 161, 71))
        self.clear.setObjectName("clear")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 190, 111, 41))
        self.label_8.setObjectName("label_8")
        Affairs.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Affairs)
        self.statusbar.setObjectName("statusbar")
        Affairs.setStatusBar(self.statusbar)

        self.retranslateUi(Affairs)
        QtCore.QMetaObject.connectSlotsByName(Affairs)

    def retranslateUi(self, Affairs):
        _translate = QtCore.QCoreApplication.translate
        Affairs.setWindowTitle(_translate("Affairs", "MainWindow"))
        self.Run.setText(_translate("Affairs", "Рассчитать"))
        self.label.setText(_translate("Affairs", "1. Запишите Ваши текущие задачи (дела, над которыми Вы работаете)\n"
"\n"
"2. Оцените каждую из перечисленных задач по двум критериям:\n"
"\n"
"- важно ли это? (варианты ответа: 1. Да; 2. Нет)\n"
"\n"
"- срочно ли это? (варианты ответа: 1. Да; 2. Нет)"))
        self.add.setText(_translate("Affairs", "Добавить"))
        self.label_6.setText(_translate("Affairs", "Важно"))
        self.label_2.setText(_translate("Affairs", "Да"))
        self.label_3.setText(_translate("Affairs", "Нет"))
        self.label_7.setText(_translate("Affairs", "Срочно"))
        self.label_4.setText(_translate("Affairs", "Да"))
        self.label_5.setText(_translate("Affairs", "Нет"))
        self.clear.setText(_translate("Affairs", "Сбросить"))
        self.label_8.setText(_translate("Affairs", "Задача"))

