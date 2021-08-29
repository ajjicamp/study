from multiprocessing import Process, current_process
import os

print('1) test')
print(os.getpid())
class Cproc:
    def __init__(self):
        print('2) class', __name__)
        print('3)', self)
        # func()
        # self.sub('이 안에서')
        print('9)init getpid: ', os.getpid())
        print('10)cur name: ', current_process())
        # Process(target=self.sub, args=('이 안에서',)).start()
        self.sub('init에서')

    def sub(self, args):
        print('4) sub', args)
        print('sub getpid: ', os.getpid())
        print('sub getppid: ', os.getppid())
        print('sub name: ', current_process())

def func(where):
    print('6)func', __name__, where)
    print('7)', os.getpid())
    print('8)', current_process())
    # func_class = Cproc()
    # func_class.sub('func에서: ')
    # Cproc()

if __name__ =='__main__':
# func()
    p = Process(target=Cproc, args=())
    p.start()
    p.join()
    print('main$$', os.getpid())
    print('main$$', current_process())
# cproc = Cproc()

