import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import ui

class ExampleApp(QtWidgets.QMainWindow, ui.Ui_Affairs):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        # self.clear.clicked.connect(self.Clear)
        self.add.clicked.connect(self.AddAffair)
    
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
        
    def Run(self):
        pass
        
        
def main():
        app = QtWidgets.QApplication(sys.argv)  
        window = ExampleApp()  
        window.show() 
        app.exec_()  


if __name__=="__main__":
        main()