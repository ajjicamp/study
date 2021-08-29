# b에서 생성한 shared_memory의 dtype과 c에서 정의하는 dtype이 같아야 안정적이다. 예 ; 'U18'
# 아래의 shm방식이 shareable방식보다 10배나 빠르다.
import numpy as np
from multiprocessing import Process, shared_memory
import time

class Main:
    def __init__(self):
        print('mainclass')
        print('b',b[0], b[-1])


def SubProc(b_shm_name, num):
    print(b_shm_name)
    exsit_shm = shared_memory.SharedMemory(create=False, name=b_shm_name)
    print('subproc_exsit:', exsit_shm)
    c = np.ndarray((2,), dtype='U18', buffer=exsit_shm.buf)
    start = time.time()

    cnt = 0
    data = None
    while True:
        cnt += 1
        c[-1] = f'change{str(cnt)}'
        # msg = f'{c[-1]}{str(cnt)}'
        if cnt > num:
            break

        data = c[-1]

    print('소요시간:', time.time() - start)
    print(f'msg {data}')

    print('subproc_c', c)


if __name__ == '__main__':
    # a = np.array([2, 4, 5, 6, 8])
    num = 1000000
    a = np.array(['삼성전자', '005930            '])
    shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
    b[:] = a[:]
    print('b[0]', b[0])
    print('dtype', b.dtype)
    print(shm.name)

    p=Process(target=SubProc, args=(shm.name, num))
    p.start()
    p.join()
    main = Main()
