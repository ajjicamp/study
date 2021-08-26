import numpy as np
from multiprocessing import Process, shared_memory
from subproc import SubProc

class Main:
    def __init__(self):
        print('mainclass')

if __name__ == '__main__':
    a = np.array([2, 4, 5, 6, 8])
    shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    # shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    # b = shared_memory.ShareableList(a)
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
    b[:] = a[:]
    print('b', b)
    print(shm.name)

    Process(target=SubProc, args=(b, shm.name)).start()
    main = Main()



