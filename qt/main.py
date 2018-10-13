import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import ui

class ExampleApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.clear.clicked.connect(self.Clear)
        self.run.clicked.connect(self.Run)

    def Clear(self):
        # self.inpMonthIncome.setText("")
        self.inpWage.setText("")
        self.inpParrentWage.setText("")
        self.inpRent.setText("")
        self.inpAllowance.setText("")
        self.inpCashback.setText("")
        self.inpSaving.setText("")
        self.anotherIncome.setText("")

        #################
        self.utilities.setText("") # not
        self.rentalOfProperty.setText("") # not
        self.loanRepayment.setText("") # not
        self.education.setText("") # not
        self.healthCare.setText("") # nor

        #####################
        self.nutrion.setText("")
        self.clothing.setText("")
        self.housewares.setText("")
        self.phoneOrInternet.setText("")
        self.directions.setText("")
        self.fines.setText("")
        self.otherExpenses.setText("")

    def Run(self):
        maxNutrionIncome = 10000 # питание
        maxDirectionsIncome =  4500 # проезд
        maxHousewaresIncome = 500 # предметы домашнего обихода
        maxClothingIncome = 1000 # одежда
        maxFinesIncome = 0 # штрафы
        maxFunIncome = 1000 # развлечения
        maxAnotherIncome = 1000 # остальные расходы

        try:
            realNutrionIncome = int(self.nutrion.text())
            realDirectionsIncome = int(self.directions.text())
            realHouseWaresIncome = int(self.housewares.text())
            realClothingIncome = int(self.clothing.text())
            realFinesIncome = int(self.fines.text())
            realFunIncome = int(self.fun.text())
            realAnotherIncome = int(self.anotherIncome.text())
        except ValueError:
            QMessageBox.about(self, "Ошибка","В некоторых полях введены не числа!")
        







def main():
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        window = ExampleApp()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно
        app.exec_()  # и запускаем приложение


if __name__=="__main__":
        main()