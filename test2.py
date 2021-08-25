# tablewidget에서 QtWidgets.QTableWidgetItem()은 한번 setItem()하면 끝이다.
# cell마다 매번 새로 생성해야한다.
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt

class TestWindow():
    def __init__(self):
        super().__init__()
        self.window = QtWidgets.QMainWindow()
        self.window.setGeometry(700,100,1200,1000)
        self.table = QtWidgets.QTableWidget(self.window)
        self.table.move(100,100)
        self.table.resize(1000,800)
        self.table.setColumnCount(5)
        self.table.setRowCount(20)
        # self.resize(1000,500)
        self.window.show()
        self.redraw()

    def redraw(self):
        li = ['SUNDAY', 'MONDAY', 'THUSEDAY', 'WENDSDAY', 'THIRTHDAY', 'FRIDAY', 'SATDAY']
        da = [0,11.234,22,330000,44,55,66]
        for row in range(7):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem())
            # self.table.item(row,0).setText(li[row])
            # self.table.
            self.table.item(row,0).setData(Qt.DisplayRole, da[row])

        '''   
        item = QtWidgets.QTableWidgetItem('SUNDAY')
        self.table.setItem(0, 0, item)
        # self.table.item(0,0).setText("TEST")
        item = QtWidgets.QTableWidgetItem('MONDATY')
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem('THUSEDAY')
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem('WENDSDAY')
        self.table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem('THIRDDAY')
        self.table.setItem(4, 0, item)

        first = 'NewWeek'
        copydata = self.table.item(0, 0).text()
        self.table.item(0, 0).setText(first)

        for row in range(1, 8):
            if self.table.item(row, 0) == None:
                self.table.setItem(row,0,QtWidgets.QTableWidgetItem())
                self.table.item(row,0).setText(copydata)
                return
            data = self.table.item(row, 0).text()
            print('data', data)
            self.table.item(row, 0).setText(copydata)
            copydata = data
        '''



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    testwindow = TestWindow()
    # testwindow.show()
    app.exec_()