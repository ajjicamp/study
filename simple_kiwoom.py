import sys
from PyQt5 import QtWidgets, QAxContainer
import pythoncom
from multiprocessing import Process
import time

app = QtWidgets.QApplication(sys.argv)
# class Worker(Process):
class Worker:
    def __init__(self, args):
        # super().__init__()
        self.connected = False
        self.ocx = QAxContainer.QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveRealData.connect(self._handler_real)
        # self.ocx.OnReceiveMsg.connect(self._handler_msg)
        self.start()
        app.exec_()
    def start(self):
        self.CommConnect(block=True)
        self.SetRealReg("1001", "005930", "20;41", "0")
        # self.eventloop =
        # self.EventLoop()

    def _handler_login(self, err_code):
        if err_code == 0:
            self.connected = True

    def _handler_real(self, code, realtype, realdata):
        print('real_data', realtype)
        if realtype == "주식체결":
            print('실시간 주식체결')

    # def EventLoop(self):
    #     while True:
    #         print('루프 동작중')
    #         time.sleep(1)

    def CommConnect(self, block=True):
        """
        로그인 윈도우를 실행합니다.
        :param block: True: 로그인완료까지 블록킹 됨, False: 블록킹 하지 않음
        :return: None
        """
        self.ocx.dynamicCall("CommConnect()")
        if block:
            while not self.connected:
                pythoncom.PumpWaitingMessages()

    def SetRealReg(self, screen, code_list, fid_list, real_type):
        ret = self.ocx.dynamicCall("SetRealReg(QString, QString, QString, QString)", screen, code_list, fid_list, real_type)
        print('ret:', ret)
        return ret

# def Main():
#     pass

if __name__ == '__main__':

    q = 'test'
    Process(target=Worker, args=(q,), daemon=False).start()
    # worker = Worker(q)
    # worker.start()
    # skiwoom = Skiwoom(q)
    app = QtWidgets.QApplication(sys.argv)
    # main = Main()
    # skiwoom = Skiwoom()
    app.exec_()
