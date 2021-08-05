import sys
import os
from multiprocessing import Process, Queue
from threading import Thread
from PyQt5 import QtWidgets
import time

class Worker():
# class Worker(Process):
# class Worker(Thread):
    def __init__(self, queue):
        # super().__init__()
        self.q = queue
        # self.msg = f'{argv} Worker Process\n'*3
        print('이름: ', __name__)
        print('parent process:', os.getppid())
        print('process id:', os.getpid())
        self.run()

    def run(self):
        print('run 이름: ', __name__)

        while True:
            if not self.q.empty():
                data = self.q.get()
                print(data)
                time.sleep(0.5)
                if data == 'terminate':
                    break
        print('finish')

class Main:
    def __init__(self, queue):
        self.q = queue

        for i in range(10):
            self.q.put(f"multi {str(i)}")

        self.q.put('terminate')



        # worker = Worker('multi')
        # worker = Process(name='worker1', target=Worker, args=('multi',))
        # worker = Thread(target=Worker, args=('multi',))
        # worker.start()


if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    queue = Queue()
    # worker = Worker('multi')
    worker = Process(name= 'worker1', target=Worker, args=(queue,))
    # worker = Thread(target=Worker, args=('multi',))
    worker.start()
    # worker = Worker('multi')
    proc = Main(queue)
    # app.exec_()
    # worker.close()
    # worker.join()
    # worker.terminate()
    # sys.exit()