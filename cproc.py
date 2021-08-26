from multiprocessing import shared_memory, Process
# import share

def cproc(b):
    c = shared_memory.ShareableList(name=b.shm.name)
    print(c)
    print(c[0])
    c[-1] = -999
    print(b[-1])
    b.shm.close()
    c.shm.close()
    c.shm.unlink()
