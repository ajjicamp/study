from multi02 import *

if __name__ == '__main__':
    queue = Queue()
    # worker = Worker('multi')
    proc = Main(queue)

    worker = Process( target=Worker, args=(queue,))
    # worker = Thread(target=Worker, args=('multi',))
    worker.start()
    # worker = Worker('multi')
