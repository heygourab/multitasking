import time, threading
# threading using for use multitasking....

def calc_cube(numbers):
    for i in numbers:
        time.sleep(0.1)
        print('cube:', i * i)


def calc_square(numbers):
    for i in numbers:
        time.sleep(0.1)
        print('square:', i * i * i)


arr = [2, 3, 8, 9]
t = time.time()

t1 = threading.Thread(target=calc_cube, args=(arr, ))
t2 = threading.Thread(target=calc_square, args=(arr, ))

t1.start()
t2.start()

t1.join()
t2.join()

print('done in:', time.time() - t)