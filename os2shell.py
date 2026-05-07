import os
from multiprocessing import Process

def child():
    print("After fork, child process ID =", os.getpid())

if __name__ == "__main__":
    print("Before fork, process ID =", os.getpid())

    p = Process(target=child)
    p.start()
    p.join()

    print("After fork, parent process ID =", os.getpid())