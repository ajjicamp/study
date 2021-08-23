import random
import time
from multiprocessing import Process, Queue
import pandas as pd

def dict_put_data(num, q):
    start = time.time()

    # for i in range(num):
    hap = 0
    while not hap >= (num - 1):
        dic = {}
        dic['code'] = '005930'
        dic['name'] = 'samsung'
        dic['현재가'] = 78000
        dic['거래량'] = 2300000
        dic['시가']  = 77000
        dic['고가']  = 79000
        dic['등략률'] = 0.55

        q.put([dic, 'dict'])
        hap += 1

    # print(dic)
    return {'dic_소요시간': time.time() - start}

def df_put_data(num, q):
    start = time.time()

    # for i in range(num):
    hap = 0
    while not hap >= (num - 1):
        dic = {}
        dic['code'] = '005930'
        dic['name'] = 'samsung'
        dic['현재가'] = 78000
        dic['거래량'] = 2300000
        dic['시가']  = 77000
        dic['고가']  = 79000
        dic['등략률'] = 0.55
        df = pd.DataFrame(dic, index=[0])
        # print('df', df)
        q.put([df, 'df'])
        hap += 1

    # print(dic)
    return {'df_소요시간': time.time() - start}

def list_put_data(num, q):
    start = time.time()
    for i in range(num):
        # li = []
        data = None
        a = '005930'
        b = 'samsung'
        c = 78000
        d = 2300000
        e = 77000
        f = 79000
        g = 0.55
        li = (a, b, c, d, e, f, g)
        # q.put((li, 'list'))
        q.put(['list', ('real',li)])

    # print(li)
    return {'li_소요시간': time.time() - start}

def tuple_put_data(num, q):
    start = time.time()
    for i in range(num):
        # data = None
        a = '005930'
        b = 'samsung'
        c = 78000
        d = 2300000
        e = 77000
        f = 79000
        g = 0.55
        # tup = (a, b, c, d, e, f, g)
        tup = (a, b, c, d, e, f, g)
        q.put(['tuple',tup, 'real'])

    return {'tup_소요시간': time.time() - start}

def data_recp(q, num, **kwargs):
    start = time.time()
    hap = 0
    sum = []
    # for i in range(num):
    while True:
        data = q.get()
        sum.append(data)
        hap += 1
        if hap >= num - 1:
            break
        # print(type(data))
    print('data', data)
    print('recp소요시간', time.time() - start)

if __name__ == '__main__':
    num = 1000000
    q = Queue()

    # p = Process(target=data_recp, args=(q, num))
    # p.start()
    # ti = dict_put_data(num, q)
    # print(f"dict소요시간  {ti['dic_소요시간']}")
    # p.join()
    # p.close()
    #
    # p = Process(target=data_recp, args=(q, num))
    # p.start()
    # ti = df_put_data(num, q)
    # print(f"df소요시간  {ti['df_소요시간']}")
    # p.join()
    # p.close()

    p = Process(target=data_recp, args=(q, num))
    p.start()
    ti = list_put_data(num, q)
    print(f"list소요시간  {ti['li_소요시간']}")
    p.join()
    p.close()

    p = Process(target=data_recp, args=(q, num))
    p.start()
    ti = tuple_put_data(num, q)
    print(f"tuple소요시간  {ti['tup_소요시간']}")
    p.join()
    p.close()