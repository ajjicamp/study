import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from multiprocessing import Process, Queue

# class Worker(QThread):
class Worker(Process):
    def __init__(self,data_queue, time_queue):
        super().__init__()
        self.data_queue = data_queue
        self.time_queue = time_queue


    def run(self):
        gross_time = 0
        gross_count = 0
        while True:
            if not self.data_queue.empty():
                get_start= time.time()
                data = self.data_queue.get()
                stime = self.time_queue.get()
                # print("총 소요시간: ", time.time() - stime[0])

                net_time = time.time() - stime[1]

                gross_time = gross_time + net_time
                gross_count += 1
                avg_net_time = gross_time / gross_count
                print("평균시간: ", avg_net_time)

                # print("sum1:", data['sum1'])
                # print("sum2:", data['sum2'])
                # print("sum3:", data['sum3'])
                # print("data: ", data)
                # print("소요시간: ", time.time() - )
                print("넘어온 get시간: ", net_time)
                print("순수 get시간: ", time.time() - get_start)



class Main:
    def __init__(self, data_queue, time_queue):
        self.data_queue = data_queue
        self.time_queue = time_queue
        self.worker = Worker(data_queue, time_queue)  # 스레드를 만드는 방법이 너무 간단? 아무것도 필요업이 queue만 전달
        # self.worker.trigger.connect()  # todo 요게 가장 중요한 핵심
        self.worker.start()

        self.queue_put()

    def queue_put(self):
        while True:
            start_time = time.time()

            sum1 = 1
            sum2 = 1
            sum3 = 1

            for i in range(1, 10000000):
                sum1 += i
            # print("sum1: ", sum1)

            for i in range(1, 100):
                sum2 = sum2 * i
            # print("sum2: ", sum2)

            for i in range(1, 1000):
                sum3 = sum3 + i^i
            # print("sum3: ", sum3)


            dic_sum = {'sum1': sum1,'sum2': sum2, 'sum3': sum3 }
            t = 'test_time'
            dic_sum['호가시간'] =t
            dic_sum['매도호가1'] = t
            dic_sum['매도호가수량1'] = t
            dic_sum['매도호가직전대비1'] = t
            dic_sum['매도호가2'] = t
            dic_sum['매도호가수량2'] = t
            dic_sum['매도호가직전대비2'] = t
            dic_sum['매도호가3'] = t
            dic_sum['매도호가수량3'] = t
            dic_sum['매도호가직전대비3'] = t
            dic_sum['매수호가1'] = t
            dic_sum['매수호가수량1'] = t
            dic_sum['매수호가직전대비1'] = t
            dic_sum['매수호가2'] = t
            dic_sum['매수호가수량2'] = t
            dic_sum['매수호가직전대비2'] = t
            dic_sum['매수호가3'] = t
            dic_sum['매수호가수량3'] = t
            dic_sum['매수호가직전대비3'] = t
            dic_sum['매도호가총잔량'] = t
            dic_sum['매도호가총잔량직전대비'] =t
            dic_sum['매수호가총잔량'] = t
            dic_sum['매수호가총잔량직전대비'] =t

            # dic_sum = [sum1, sum2, sum3 ]
            # t = 'test_time'
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)
            # dic_sum.append(t)

            self.data_queue.put(dic_sum)
            # print("소요시간: ", time.time() - start_time)

            time_data = (start_time, time.time())
            self.time_queue.put(time_data)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    data_queue = Queue()
    time_queue = Queue()

    main = Main(data_queue, time_queue)
    app.exec_()
