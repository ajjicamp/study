from multiprocessing import Manager
if __name__ == '__main__':
    manager = Manager()
    l = manager.list([i*i for i in range(10)])
    print(l)
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(str(l))
    print(repr(l))
    # <ListProxy object, typeid 'list' at 0x...>
    print(l[4])
    # 16
    print(l[2:5])
    # [4, 9, 16]
