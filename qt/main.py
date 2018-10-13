import sys
from PyQt5 import QtWidgets
import ui

class ExampleApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.Clear)
        self.pushButton_2.clicked.connect(self.Check)

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
        self.utilities.setText("")
        self.rentalOfProperty.setText("")
        self.loanRepayment.setText("")
        self.education.setText("")
        self.healthCare.setText("")
        self.nutrion.setText("")
        self.clothing.setText("")
        self.housewares.setText("")
        self.phoneOrInternet.setText("")
        self.directions.setText("")
        self.fines.setText("")
        self.otherExpenses.setText("")

    def Check(self):
        print(self.inpWage.text())

def main():
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        window = ExampleApp()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно
        app.exec_()  # и запускаем приложение


if __name__=="__main__":
        main()