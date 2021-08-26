from multiprocessing.managers import SharedMemoryManager
from multiprocessing import Process,shared_memory

smm = SharedMemoryManager()
smm.start()  # Start the process that manages the shared memory blocks
sl = smm.ShareableList(range(4))
raw_shm = smm.SharedMemory(size=128)
another_sl = smm.ShareableList('alpha')
smm.shutdown()  # Calls unlink() on sl, raw_shm, and another_sl

with SharedMemoryManager() as smm:
     # Divide the work among two processes, storing partial results in sl
     sl = smm.ShareableList(range(2000))
     p1 = Process(target=do_work, args=(sl, 0, 1000))
     p2 = Process(target=do_work, args=(sl, 1000, 2000))
     p1.start()
     p2.start()  # A multiprocessing.Pool might be more efficient
     p1.join()
     p2.join()   # Wait for all work to complete in both processes
     total_result = sum(sl)  # Consolidate the partial results now in sl

def do_work(sl, start, end):
    print(sl)