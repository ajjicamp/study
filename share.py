from multiprocessing import shared_memory, Process
from cproc import cproc

print('mainprocess')
# b = shared_memory.ShareableList(range(5))

# def cproc():
#     c = shared_memory.ShareableList(name=b.shm.name)
#     print(c)
#     c[-1] = -999
#     print(b[-1])
#     b.shm.close()
#     c.shm.close()
#     c.shm.unlink()

if __name__ == '__main__':
    b = shared_memory.ShareableList(range(5))
    Process(target=cproc, args=(b,)).start()