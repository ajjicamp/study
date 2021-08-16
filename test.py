import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QColor

class Wintest(QtWidgets.QMainWindow):
    def __init__(self):
        super(Wintest, self).__init__()
        qfont20 = QFont()
        qfont20.setFamily('나눔고딕')
        qfont20.setPixelSize(20)
        self.qfont20 = qfont20

        self.setGeometry(800,400,1000,500)
        self.setWindowTitle("mainwindow$$")
        self.resize(1000, 500)
        # self.show()

        # pushbutton = QtWidgets.QPushButton('test', self)
        # pushbutton.clicked.connect(lambda: self.pushbutton_clicked('why lambda??'))

        # self.dialog = QtWidgets.QDialog()
        self.dialog = QtWidgets.QWidget()
        # pushbutton01 = QtWidgets.QPushButton()
        # self.setPushbutton()
        # pushbutton01 = self.setPushbutton('test', self, self.pushbutton_clicked, 'why')

    # def setPushbutton(self):     # 함수가 반드시 필요한 건 아니다.
        # app = QtWidgets.QApplication(sys.argv)
        btn = QtWidgets.QPushButton('test', self.dialog)
        btn.setFont(self.qfont20)
        btn.move(100,100)
        btn.clicked.connect(lambda: self.pushbutton_clicked('how'))
        # btn.setWindowModality(Qt.NonModal)
        # btn.setGeometry(100, 100, 100, 50)
        btn.resize(100, 50)

        # QDialog 세팅
        self.dialog.setWindowTitle('Dialog')
        # self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.setWindowModality(Qt.NonModal)
        self.dialog.resize(500, 400)
        # todo 이것이 중요
        self.dialog.show()

        # btn.show()
        # app.exec_()

    def pushbutton_clicked(self, msg):
        print('button clicked', msg)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wintest = Wintest()
    wintest.show()
    app.exec_()