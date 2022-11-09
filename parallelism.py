import threading
from time import *

def proc(n):
    sleep(int(n))
    print("Процесс", n)


p1 = threading.Thread(target=proc, name="t1", args=["1"])
p2 = threading.Thread(target=proc, name="t2", args=["2"])
p1.start()
p2.start()