import numpy as np
from multiprocessing import Process, shared_memory, Array
import time

class Main:
    def __init__(self):
        print('mainclass')
        print('main_a', a.get_obj().value)


def SubProc(a, num):
    # print(b_shm_name)
    # exsit_shm = shared_memory.SharedMemory(create=False, name=b_shm_name)
    # print('subproc_exsit:', exsit_shm)
    # b = np.ndarray((2,), dtype='U18', buffer=exsit_shm.buf)
    print('a', a)
    start = time.time()

    cnt = 0
    while True:
        cnt += 1
        a.get_obj().value = f'change {str(cnt)}'
        # 여기서 바로 값을 얻는 걸로 테스트
        data = a.get_obj().value


        if cnt > num:
            break

    print('소요시간:', time.time() - start)
    print('a_value', a.get_obj().value)
    print(data)


if __name__ == '__main__':
    # a = np.array([2, 4, 5, 6, 8])
    num = 1000000
    a = Array('u', 15)
    # ['삼성전자', '005930            '])
    print('init_a', a)
    # shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    # b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
    # b[:] = a[:]
    # print('b[0]', b[0])
    # print('dtype', b.dtype)
    # print(shm.name)

    p=Process(target=SubProc, args=(a, num))
    p.start()
    p.join()
    main = Main()
