from multiprocessing import shared_memory
import numpy as np

class SubProc:
    def __init__(self, b, b_shm_name):
        print(b_shm_name)
        exsit_shm = shared_memory.SharedMemory(create=False, name=b_shm_name)
        print('subproc_exsit:', exsit_shm)
        c = np.ndarray((5,), dtype=np.int32, buffer=exsit_shm.buf )
        print('subproc', c)

if __name__ == '__main__':
    subproc = SubProc()
