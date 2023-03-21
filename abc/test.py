import time
import threading


def test1():
    time.sleep(1)
    print("1")

def test2():
    time.sleep(1)
    print(2)

x = threading.Thread(target=test1)
y = threading.Thread(target=test2)

x.start()
y.start()

x.join()
y.join()