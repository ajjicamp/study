# 미완성
from multiprocessing import Process, Manager, Queue
import time

def f(q, d, l, num):
    start = time.time()
    # d = {}
    cnt = 0
    while True:
        data = f'test {cnt}'
        d['default'] = f'test {str(cnt)}'
        data1 = d['default']
        # d['2'] = 2
        # d[0.25] = None
        # l.reverse()
        # q.put(d)
        # data = q.get()
        cnt += 1
        if cnt > num:
            break
    # cnt = 0
    # while True:
    #     if not d == None:
    #         save = d
    #         save1 = l
    #         q.put(data)
    #         val = q.get()
        #
        # print('값이 있다')
        # cnt += 1
        # if cnt > 100000:
        #     break

    print('소요시간:', time.time() - start)
    print('크기', len(data))
    print('data', data)

if __name__ == '__main__':
    '''
    num = 1000000
    q = Queue()
    d = {}
    l = []
    p = Process(target=f, args=(q, num))
    p.start()
    p.join()
    # f(d, l, num)
    # data = q.get()
    # print(data)
    with Manager() as manager:
        num = 1000
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l, num))
        p.start()
        p.join()

    '''

    with Manager() as manager:
        q = Queue()
        num = 100000

        d = manager.dict()
        l = manager.list()
        # d = 1
        # l = 2
        p = Process(target=f, args = (q, d, l, num))
        p.start()
        p.join()

    # print('q', q.get())