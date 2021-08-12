import multiprocessing
import sys
import os
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from multiprocessing import Pool, Process, Queue, current_process
import matplotlib.pyplot as plt

app = QApplication(sys.argv)

# 한글폰트 깨짐방지
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결

form_class01 = uic.loadUiType('C:/Users/USER/PycharmProjects/study/window01.ui')[0]
form_class02 = uic.loadUiType('C:/Users/USER/PycharmProjects/study/window02.ui')[0]
form_class03 = uic.loadUiType('C:/Users/USER/PycharmProjects/study/window03.ui')[0]

class MyWindow(QMainWindow,form_class01):
    def __init__(self, num):
        super().__init__()
        self.q = Queue()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.SubWindow_clicked)
        self.pushButton_2.clicked.connect(self.SubWindow02_clicked)
        # print('pname: ', current_process().name)
        # print('main:', self)
        self.show()
        app.exec_()

    def SubWindow_clicked(self):
        SubWindow(self, self.q)

    def SubWindow02_clicked(self):
        SubWindow02(self, self.q)

class SubWindow(QMainWindow, form_class02):
    def __init__(self, parent, queue):
        # app = QApplication(sys.argv)
        super(SubWindow, self).__init__(parent)
        print('self:', self)
        self.q = queue
        self.setupUi(self)
        self.draw02()
        self.show()
        print('sub01: ', current_process().name)

    def draw02(self):
        item = QTableWidgetItem('str_test')
        self.tableWidget.setItem(1, 1, item)

class SubWindow02(QDialog, form_class03):
    def __init__(self, parent, queue):
        super(SubWindow02, self).__init__(parent)
        print('sub02:', parent)
        self.q2 =queue

        self.setupUi(self)
        self.show()
        print('sub02: ', current_process().name)


if __name__ == '__main__':
    # queue = Queue()
    # # app = QApplication(sys.argv)
    # Process(target=MyWindow, args=(queue,)).start()
    p = Pool(5)
    p.map(MyWindow, [1])


    # mainwindow = MyWindow()
    # mainwindow.show()
    # app.exec_()