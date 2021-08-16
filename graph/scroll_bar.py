# scroll bar 이용하는 방법이나 내가 원하는 형태는 아니다. 화면이 커지지 않고 제한된 범위내에서만 작동
import sys
from PyQt5.QtWidgets import *
# from PyQt4.QtGui import *
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyWindow(QWidget):
    def __init__(self):
        #super().__init__()
        super(MyWindow,self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 600)
#


        self.textEdit = QTextEdit()
        self.combo = QComboBox()
        self.pushButton= QPushButton('save')
        self.table1= QTableWidget()
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        fig, axes = plt.subplots(3,3,figsize=(5,3))
        count = 0
        for ax in axes.flatten():
            ax.plot([count,1,2,3,count*(-1)])
        self.canvas = FigureCanvas(fig)
        tab1 = QScrollArea()
        tab1.setWidget(self.canvas)
        tab1_layout = QVBoxLayout(tab1.widget())
        fig.set_tight_layout(True)
#
        tab2 = QWidget()
        self.tabs.addTab(tab1,"Tab 1")
        self.tabs.addTab(tab2,"Tab 2")
        self.tabs.tabCloseRequested.connect(self.closeTab)
#
#
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        # layout.addWidget(self.textEdit)
        # layout.addWidget(self.combo)
#         layout.addWidget(self.pushButton)
#         layout.addWidget(self.table1)
#         layout.setStretchFactor(self.tabs,5)
#         layout.setStretchFactor(self.textEdit,2)
        self.setLayout(layout)
#
    def closeTab(self,index):
        self.tabs.removeTab(index)
#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

