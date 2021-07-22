# pyqtsignal + qthread + queue 사용방법

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
from multiprocessing import Queue


# 실시간으로 들어오는 데이터를 보고 주문 여부를 판단하는 스레드
class Worker(QThread):
    # argument는 없는 단순 trigger
    # 데이터는 queue를 통해서 전달됨
    trigger = pyqtSignal()

    def __init__(self, data_queue, order_queue):
        super().__init__()
        self.data_queue = data_queue                # 데이터를 받는 용
        self.order_queue = order_queue              # 주문 요청용
        self.timestamp = None
        self.limit_delta = datetime.timedelta(seconds=2)   # 2초 간격

    def run(self):
        while True:
            if not self.data_queue.empty():
                data = self.data_queue.get()              # queue에서 데이터를 얻어옴
                result = self.process_data(data)          # 주문여부를 판단하는 함수를 호출하여 값을 저장.
                if result:                                # 결과가 true이면
                    self.order_queue.put(data)                      # 주문 Queue에 주문을 넣음 # 여기서 왜 data를 전달하는가
                    self.timestamp = datetime.datetime.now()        # 이전 주문 시간을 기록함
                    self.trigger.emit()                             # pyqtsignal 실행

    # 주문여부를 판단하는 함수.
    def process_data(self, data):
        # 시간 제한을 충족하는가?
        time_meet = False
        if self.timestamp is None:                                  # 이전 주문시간이 없으면 즉, 첫 주문이다.?
            time_meet = True
        else:
            now = datetime.datetime.now()                           # 현재시간
            delta = now - self.timestamp                            # 현재시간 - 이전 주문 시간
            if delta >= self.limit_delta:                           # 이전주문시간대비 현재시간 경과시간이 2초이상이면
                time_meet = True

        # 알고리즘을 충족하는가?
        algo_meet = False
        if data % 2 == 0:                                           # 짝수이면?
            algo_meet = True

        # 알고리즘과 주문 가능 시간 조건을 모두 만족하면
        if time_meet and algo_meet:
            return True
        else:
            return False


class MyWindow(QMainWindow):
    def __init__(self, data_queue, order_queue):
        super().__init__()

        # queue
        self.data_queue = data_queue
        self.order_queue = order_queue

        # thread start
        self.worker = Worker(data_queue, order_queue)  # 스레드를 만드는 방법이 너무 간단? 아무것도 필요업이 queue만 전달
        self.worker.trigger.connect(self.pop_order)    # todo 요게 가장 중요한 핵심
        self.worker.start()

        # 데이터가 들어오는 속도는 주문보다 빠름
        self.timer1 = QTimer()
        self.timer1.start(1000)             # QTimer()실행. ------> 1초마다 실행
        self.timer1.timeout.connect(self.push_data)  # 타임아웃되면 실행하는 slot

    def push_data(self):
        now = datetime.datetime.now()
        self.data_queue.put(now.second)         # 현재시간 중 초 부분만 data_queue애 전달.

    @pyqtSlot()
    def pop_order(self):
        if not self.order_queue.empty():
            data = self.order_queue.get()
            print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    data_queue = Queue()
    order_queue = Queue()
    window = MyWindow(data_queue, order_queue)
    window.show()

    app.exec_()


'''
multiprocessing pyqtsignal을 정리하자면
1) multiprocessing.Queue()를 생성하여 main모듈인 MyWindow()클래스에 인자로 전달
2) MyWindow()에서는 생성자에서 전달받은 queue를 전역함수로 사용하기 위하여 self.queue변수에 저장.
3) 부분작업을 처리할 thread를 queue를 포함하여 만들고, pyqtsignal을 연결할 slot을 지정한 후 thread를 start()
4) 전체적인 작업은 Mywindow에서 data를 queue를 이용하여 thread에 넘겨주고 thread는 queue에서 data를 꺼내서 주문여부를 판단하고
   조건이 충족되면 주문 queue에 data를 put
5) 이제 pyqtslot(이 슬롯은 MyWindow에 설정되어 있다)에서 주문queue의 데이터를 꺼내서 슬롯의 명령을 실행한다
 '''