import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import ui
from functools import reduce

class ExampleApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.clear.clicked.connect(self.Clear)
        self.run.clicked.connect(self.Run)

    def Clear(self):
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
        checkList = [
        self.inpWage.text(),
        self.inpParrentWage.text(),
        self.inpRent.text(),
        self.inpAllowance.text(),
        self.inpCashback.text(),
        self.inpSaving.text(),
        self.anotherIncome.text(),
        self.utilities.text(),
        self.rentalOfProperty.text(),
        self.loanRepayment.text(),
        self.education.text(),
        self.healthCare.text(),
        self.nutrion.text(),
        self.clothing.text(),
        self.housewares.text(),
        self.phoneOrInternet.text(),
        self.directions.text(),
        self.fines.text(),
        self.otherExpenses.text()
        ] 

        for i in checkList:
            if len(i) == 0:
                QMessageBox.about(self, "Ошибка","Заполните все поля!")
                return
        
        for i in checkList:
            try:
                int(i)
            except ValueError:
                QMessageBox.about(self, "Ошибка","В некоторых полях введены не числа!")
                return
        

        self.firstRecomendation = ''' 
        Очевидно, Вы лишены способности принимать взвешенные финансовые решения. Срочно учитесь планировать свои траты. Что можно предложить:
- создавайте резервы под крупные покупки, для этого четко определитесь с размером ежемесячного взноса в Ваш резерв. Запретите себе пользоваться резервом без крайней необходимости;
- иногда разрешайте себе расслабиться и потратить больше, чем нужно. Главное, чтобы потраченная сумма не выходила за пределы выделенного Вами бюджета.
Помните, если бы нужно было выбрать самый главный совет по обращению с деньгами, гарантированно позволяющий разбогатеть каждому, совет был бы таким: «Сначала инвестируйте, а потом тратьте оставшиеся деньги».
        '''

        self.secondRecomendation =  '''
        Очевидно, Вам знакомо понятие «экономия». Финансово состоятельные люди, когда им задают вопрос о залоге финансового благополучия, отвечают: «нужно рационально, а не эмоционально тратить зарабатываемые деньги». Деньги должны работать, а не тратиться. Поэтому покупайте качественные вещи по низким ценам, торгуйтесь, требуйте скидок. 
Вместе с тем, не забывайте, что «Стать богатым легко. Трудно продолжать быть богатым» - это слова Пола Петти, самого богатого человека в мире в середине ХХ века.
А потому оттачивайте умение сохранять и удерживать свой капитал.
        '''
        
        self.thirdRecomendation = '''
        Богатый – не тот, кто зарабатывает, а тот, кто не тратит. Можно жить в достатке при любом доходе, нужно лишь научиться экономить правильно. Вот лишь несколько рекомендаций, которые, как показывает практика, весьма эффективны:
- никогда не ходите в магазин на голодных желудок;
- после получения заработка – сразу домой, чтобы перед грядущими тратами успел включиться холодный рассудок, а не горячая голова;
- не делайте спонтанных покупок, дайте себе несколько дней на раздумья: так нужна ли Вам эта покупка;
- не берите в долг;
- не давайте в долг;
- откажитесь от вредных привычек. 
Еще Бенджамин Франклин сказал: «Остерегайтесь мелких напрасных расходов, ибо маленькая течь может потопить большой корабль». Возьмите это за правило.
        '''

        incomes = [
        int(self.inpWage.text()),
        int(self.inpParrentWage.text()),
        int(self.inpRent.text()),
        int(self.inpAllowance.text()),
        int(self.inpCashback.text()),
        int(self.inpSaving.text()),
        int(self.anotherIncome.text()),
        ]

        maxNutrionExpenses = 10000 # питание
        maxDirectionsExpenses =  4500 # проезд
        maxHousewaresExpenses = 500 # предметы домашнего обихода
        maxClothingExpenses = 1000 # одежда
        maxFinesExpenses = 0 # штрафы
        maxFunExpenses = 1000 # развлечения
        maxAnotherExpenses = 1000 # остальные расходы
       

        realNutrionExpenses = int(self.nutrion.text())
        realClothingExpenses = int(self.clothing.text())
        realHouseWaresExpenses = int(self.housewares.text())
        realDirectionsExpenses = int(self.directions.text())
        realFinesExpenses = int(self.fines.text())
        realFunExpenses = int(self.fun.text())
        realAnotherExpenses = int(self.otherExpenses.text())
          
        self.economy = 0 # экономия 

        if realAnotherExpenses > maxAnotherExpenses:
            self.economy += realAnotherExpenses - maxAnotherExpenses
        if realDirectionsExpenses > maxDirectionsExpenses:
            self.economy += realDirectionsExpenses - maxDirectionsExpenses
        if realHouseWaresExpenses > maxHousewaresExpenses:
            self.economy += realHouseWaresExpenses - maxHousewaresExpenses
        if realClothingExpenses > maxClothingExpenses:
            self.economy += realClothingExpenses - maxClothingExpenses
        if realFinesExpenses > maxFinesExpenses:
            self.economy += realFinesExpenses - maxFinesExpenses
        if realFunExpenses > maxFunExpenses:
            self.economy += realFunExpenses - maxFunExpenses
        if realAnotherExpenses > maxAnotherExpenses:
            self.economy += realAnotherExpenses - maxAnotherExpenses

        self.finalAnswer = ""

        finalIncome = reduce(lambda x,y:x+y,incomes)

        firstResult = finalIncome * 0.2
        secondResult = finalIncome * 0.05

        if self.economy > firstResult:
            self.finalAnswer = self.firstRecomendation
        elif self.economy <= firstResult and self.economy >= secondResult:
            self.finalAnswer = self.secondRecomendation
        elif self.economy < secondResult:
            self.finalAnswer = self.thirdRecomendation

        QMessageBox.about(self, "Экономия","Вы могли бы сэкономить: "+str(self.economy)+"\n"+self.finalAnswer)


def main():
        app = QtWidgets.QApplication(sys.argv)  
        window = ExampleApp()  
        window.show() 
        app.exec_()  


if __name__=="__main__":
        main()