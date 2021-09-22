# 미완성
from multiprocessing import Process, Manager, Queue
import time
import pandas as pd

def f(q, d, li, num):
    d['default'] = 'sucess'
    # li.append('kim')
    # data = ('a', 'b', 'c')
    data = {'c1':'a', 'c2':'b', 'c3':'c'}
    df = pd.DataFrame(data, index=[0])
    # df = pd.DataFrame(data, columns=['c1'])
    print('df', df)

    # li.append(data)
    li.append(df)
    # li = data

    # start = time.time()
    # d = {}
    # cnt = 0
    # while True:
    #     data = f'test {cnt}'
    #     d['default'] = f'test {str(cnt)}'
    #     data1 = d['default']
        # d['2'] = 2
        # d[0.25] = None
        # l.reverse()
        # q.put(d)
        # data = q.get()
        # cnt += 1
        # if cnt > num:
        #     break
    # print('소요시간:', time.time() - start)
    # print('크기', len(data))
    # print('data', data)

if __name__ == '__main__':

    # with Manager() as manager:
    q = Queue()
    num = 100000

    d = Manager().dict()
    li = Manager().list()
    p = Process(target=f, args=(q, d, li, num))
    p.start()
    p.join()

    print('d', d)
    print('li', li)
    print(li[0]['c2'])
    print(type(li[0]))