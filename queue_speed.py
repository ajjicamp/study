import sys
from PyQt5 import QtCore, QtWidgets
from multiprocessing import Process, Queue, shared_memory, Array
import time
import pythoncom
import datetime

class Main:
    def __init__(self):
        print(__name__)

def sub_rec(q, num):
    def now():
        return datetime.datetime.now()

    start = time.time()
    data = ""
    cnt = 0
    while True:
        if not q.empty():
            data = q.get()
            cnt += 1
            if cnt % 500000 == 0:
                print('qsize', q.qsize())

            if cnt > num:
                break

        '''
        time_loop = now() + datetime.timedelta(seconds=0.25)
        # print(now(), time_loop)
        while now() < time_loop:
            pythoncom.PumpWaitingMessages()
            time.sleep(0.0001)
        '''
    print('mainQ', data)
    print('mainQ소요시간', time.time() - start)


def SubProc(q, num):

    start = time.time()
    cnt = 0
    while True:
        cnt += 1
        data = f'change {str(cnt)}'
        q.put(data)
        if not q.empty():
            data = q.get()
        # if cnt % 10000 == 0:
        #     time.sleep(0.000001)
        if cnt > num:
            break


    print('put소요시간:', time.time() - start)
    print('q_value', data)

if __name__ == '__main__':

    num = 100000
    q = Queue()

    p = Process(target=SubProc, args=(q, num))
    p.start()

    # p = Process(target=sub_rec, args=(q, num))
    # p.start()

    # app =QtWidgets.QApplication(sys.argv)
    main = Main()
    # app.exec_()