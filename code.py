import time
from threading import Thread
# Multithreading is a technique where multiple are spawned
# by a process to do different tasks, at about the same time,
# just one after the other, This gives you the illusion that
# running in parallel, but they are actually run in a
# concurrent manner. In Python, the Global Interpreter Lock
# prevents the threads form running simultaneously.


def calc_cube(numbers):
    for i in numbers:
        time.sleep(0.1)
        print('cube:', i**3)


def calc_square(numbers):
    for i in numbers:
        time.sleep(0.1)
        print('square:', i**2)


if __name__ == '__main__':

    arr = [2, 3, 8, 9]
    t = time.time()

    t1 = Thread(target=calc_cube, args=(arr, ))
    t2 = Thread(target=calc_square, args=(arr, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('done in:', time.time() - t)