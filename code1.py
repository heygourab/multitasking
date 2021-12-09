import time
from multiprocessing import Process

# Multiprocessing: is a technique where parallelism in its truest form is achieved.
# Multi process are run across multiple CPU cores, which do not share the resources
# among them. Each process can have many threads running in its own memorory space.
# In python, each process has its own instance of Python interpreter doing the job
# of executing the instructions

# Every  process has its own address space(Virtual Memory). Thus program variable
# are not shared between two process. You need to use interprocess communication(IPC)
# techniques of you want to share data between two processes.

cube_list = []


def cube(nums):
    for num in nums:
        time.sleep(1)
        print(f"cube: {num * num * num }")
        cube_list.append(num * num * num)
    print(f'within a process result: {cube_list}')


# def square(nums):
#     for num in nums:
#         time.sleep(10)
#         print(f"square: {num * num}")

if __name__ == '__main__':
    arr = [2, 4, 6, 8]
    t = time.time()
    p1 = Process(target=cube, args=(arr, ))
    # p2 = Process(target=square, args=(arr, ))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()

    print('list:', cube_list)
    print('Done in:', time.time() - t)
