from multiprocessing import Pool, Process

import os

import multiprocessing as mp

from multiprocessing import Pool, Process

import threading

import time

import datetime


def multiprocess():
    start = int(time.time())

    ojbect_list = []

    for i in range(1, 12):
        task = Process(target=work_func, args=(i,))

        ojbect_list.append(task)

        task.start()

    print(f'obj01 {ojbect_list[0]}')

    for task in ojbect_list:
        task.join()

    end = int(time.time())

    print("***run time(sec) : ", end - start)

    print("Number of Core : " + str(mp.cpu_count()))


def work_func(x):
    print("time : " + str(datetime.datetime.today()) + " value :" + str(x) + " PID : " + str(os.getpid()))


if __name__ == '__main__':
    # execute only if run as a script

    multiprocess()
