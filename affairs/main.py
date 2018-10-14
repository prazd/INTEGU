import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import ui

class ExampleApp(QtWidgets.QMainWindow, ui.Ui_Affairs):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        # self.clear.clicked.connect(self.Clear)
        self.Run.clicked.connect(self.Check)
    
    def Check(self):
        self.fListWidget.addItem("...")


def main():
        app = QtWidgets.QApplication(sys.argv)  
        window = ExampleApp()  
        window.show() 
        app.exec_()  


if __name__=="__main__":
        main()