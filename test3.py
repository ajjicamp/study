import sys
from PyQt5 import QtWidgets, uic
formclass = form_class = uic.loadUiType('C:/Users/USER/PycharmProjects/study/mwindow.ui')[0]

class MainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    app.exec_()