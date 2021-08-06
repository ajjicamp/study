import sys
from simple_kiwoom import Worker
from PyQt5.QtWidgets import QWidget, QApplication
from multiprocessing import Process

class Main:
    def __init__(self):
        print("main")

if __name__ == '__main__':
    q = 'test'
    Process(target=Worker, args=(q,), daemon=False).start()
    # worker = Worker(q)
    # worker.start()
    # skiwoom = Skiwoom(q)
    app = QApplication(sys.argv)
    # main = Main()
    # skiwoom = Skiwoom()
    main = Main()
    app.exec_()
