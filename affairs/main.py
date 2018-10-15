import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import ui
from functools import reduce

class ExampleApp(QtWidgets.QMainWindow, ui.Ui_Affairs):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.add.clicked.connect(self.AddAffair)
        self.Run.clicked.connect(self.Result)
    
    def AddAffair(self):
        if len(self.affair.text()) == 0:
            QMessageBox.about(self, "Ошибка","Вы не записали задачу")
            return
        
        fYesState = self.fYes.isChecked()
        fNoState = self.fNo.isChecked()
        sYesState = self.sYes.isChecked()
        sNoState = self.sNo.isChecked()

        if fYesState == True and sYesState == True:
            self.fListWidget.addItem(self.affair.text()) # 1
        if fYesState == True and sNoState == True:
            self.sListWidget.addItem(self.affair.text()) # 2
        if fNoState == True and sYesState == True:
            self.tListWidget.addItem(self.affair.text()) # 3
        if fNoState == True and sNoState == True:
            self.lListWidget.addItem(self.affair.text()) # 4
        
    def Result(self):
        self.firstAnswer = '''
Не Вы управляете своей жизнью, а горящие сроки управляют Вами. У Вас отсутствует стратегический подход к решению проблем. В результате прямо сейчас у Вас нет ни сил, ни времени на то, чтобы задуматься о своей жизни, строить перспективные планы. Вы догоняете уходящий поезд и можете в один прекрасный день выгореть эмоционально. Нельзя жить в постоянном стрессе и кризисе! Непрерывный стресс убивает вначале способности мыслить и анализировать, затем возникают проблемы со здоровьем. Стресс и кризис – Ваш образ жизни, привычка. Будьте осторожны, так как рискуете стать зависимыми от своих дел, а значит будете чувствовать себя ненужным, если на какое-то время список срочных и важных зада иссякнет.

Научитесь делегировать свои обязанности, пересмотрите свои приоритеты. В противном случае Вы рискуете превратиться в «рабочую лошадку», живущую только работой. Никогда не забывайте, что работоголики чрезвычайно редко добиваются большого успеха или

получают повышение, продолжая изо дня в день тянуть воз задач, которые нежадные коллеги будут регулярно Вам подкидывать.

Планируйте свою жизнь, расставляйте по местам свои дела, учитесь делегировать обязанности.
        '''

        self.secondAnswer = '''
        Вас можно искренне поздравить!

Вы умеете «отделять зерна от плевел». У Вас достаточно времени, чтобы задуматься о своей жизни, строить планы на будущее, а главное – выбирать, чем и когда заняться.

Очевидно, у Вас налажен контакт с коллегами и друзьями, поскольку у Вас всегда находится время на дружеские посиделки или звонки. Если Вы сталкиваетесь с трудным вопросом – Вам есть к кому обратиться за советом.

Вы не тратите время на решение чужих проблем, умеете делегировать свои обязанности. Вы цените свое время, и, похоже, нашли именно Ваш темп жизни.
        '''

        self.thirdAnswer = '''
Для Вас настала пора задаться вопросом: почему именно Вы выполняете самую неважную часть работы? Быть может, Вы сами определили, что для Вас является основным делом, а что – лишь суета сует. Однако же имеет смысл задуматься: раз Вы сами признаете, что тратите время на выполнение неважных задач, для чего Вы так делаете?

Судя по всему, у Вас отсутствуют четкие жизненные ориентиры и планы на будущее. Если же Вы при этом будете и впредь саботировать действительно важные дела, то рискуете сами пострадать от своего выбора.

Для начала приведите в порядок свои дела, станьте незаменимым и по-настоящему нужным. Немедленно пересмотрите весь список своих приоритетов и время, которое Вы тратите на выполнение обязанностей. Вы прозябаете в кризисе застоя и без решительных действий, без четкой жизненной позиции он может окончиться плачевно.
        '''

        self.lastAnswer = '''
Неужели Вам не жаль тратить свою жизнь на выполнение никчемных дел?

Вы сконцентрированы на своих сиюминутных желаниях, которые не имеют ничего общего с поставленными когда-то перед собой целями.

Желания сбивают Вас с намеченного пути, а потому действительно значимые жизненные результаты постоянно откладываются.
        '''
        self.AswerForBestCombination = '''
        Вы – целеустремленный человек, грамотно планирующий свое будущее. Вы умеете правильно распределять свое время, не погружаясь в рутину. Вы – на верном пути, так держать!
        '''

        fCount = self.fListWidget.count()
        sCount = self.sListWidget.count()
        tCount = self.tListWidget.count()
        lCount = self.lListWidget.count()


        checkList = [fCount,sCount,tCount,lCount]
        if reduce(lambda x,y:x+y,checkList) == 0:
            QMessageBox.about(self, "Ошибка","Вы не распределили задачи!")
            return
        
        fCheck = fCount == 0 or fCount == 1
        sCheck = sCount > tCount
        lCheck = lCount == 0 or lCount == 1

        if fCheck == True and sCheck == True and lCheck == True:
            QMessageBox.about(self, "Результат",self.AswerForBestCombination)
            return
        elif fCount > sCount and fCount > tCount and fCount > lCount:
            QMessageBox.about(self, "Результат",self.firstAnswer)
            return
        elif sCount > fCount and sCount > tCount and sCount > lCount:
            QMessageBox.about(self, "Результат",self.secondAnswer)
            return
        elif tCount > fCount and tCount > sCount and tCount > lCount:
            QMessageBox.about(self, "Результат",self.thirdAnswer)
            return
        elif lCount > fCount and lCount > sCount and lCount > tCount:
            QMessageBox.about(self, "Результат",self.lastAnswer)
            return

        # Clean Button ...

       

       
        
def main():
        app = QtWidgets.QApplication(sys.argv)  
        window = ExampleApp()  
        window.show() 
        app.exec_()  


if __name__=="__main__":
        main()