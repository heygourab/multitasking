# lock🔒
# why lock?
# >> when more then one process at same time access same memory address that
# cause some problem aka bug. So we use lock, lock prevent more then one process
# to access the same memory address at a sme time.

import time
from multiprocessing import Process, Value, Lock


def deposit(value, lock):
    for i in range(100):  # loop start
        time.sleep(0.01)
        lock.acquire()  # lock is acquired
        value.value += 1  # add 1 to value
        lock.release()  # lock is released


def withdraw(value, lock):
    for i in range(100):  # loop start
        time.sleep(0.01)
        lock.acquire()  # lock is acquire
        value.value -= 1  # remove 1 from value
        lock.release()  # lock is release
    print('inner value:', value.value)


if __name__ == "__main__":
    value = Value('i', 200)  # default value: 200
    lock = Lock()

    d = Process(target=deposit, args=(
        value,
        lock,
    ))  #deposit process

    w = Process(target=withdraw, args=(
        value,
        lock,
    ))  # withdraw process

    d.start()  # Process start
    w.start()  # Process start

    d.join()  # process join to main process
    w.join()  # process join to main process

    print('outer value: ', value.value)  #print outer value
