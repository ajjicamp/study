from multiprocessing import shared_memory, Process
import time

print('mainprocess')
def start(num):
    print(f'main->b {b[-1]}')

    cnt = 0
    # while True:
    #     cnt +=1
    #
    #     if cnt > num:
    #         break

def share_sub(b, num):
    c = shared_memory.ShareableList(name=b.shm.name)
    cnt = 0
    print('c-1', c[-1])
    start = time.time()
    data = None
    while True:
        cnt += 1
        c[-1] = f'change {str(cnt)}'
        # msg = f'{c[-1]}{str(cnt)}'
        data = c[-1]
        if cnt > num:
            break

    print('소요시간:', time.time() - start)
    # print(f'msg {c[-1]}')
    print(f'msg {data}')
    # while True:

    print(f'b[-1]: {b[-1]} c[-1] {c[-1]}')
    b.shm.close()
    c.shm.close()
    c.shm.unlink()

if __name__ == '__main__':
    # b = shared_memory.ShareableList(range(5))
    num = 1000000
    b = shared_memory.ShareableList(['key', 'value          '])
    print(b)
    p = Process(target=share_sub, args=(b,num))
    p.start()
    # p.join()

    # print('b', b[-1])
    start(num)