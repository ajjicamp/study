import threading


def startTimer():
    print("Timer")
    timer = threading.Timer(5, startTimer)
    timer.start()


if __name__ == '__main__':
    startTimer()
