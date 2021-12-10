# Sharing Data Between Processes Using Queue
from multiprocessing import Process, Queue


def calc_square(nums, q):
    for i in nums:
        q.put(i * i)
        pass


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    q = Queue()
    p = Process(target=calc_square, args=(nums, q))
    p.start()
    p.join()
    while q.empty() is False:
        print(q.get())

# what is deference between Multiprocessing Queue and Queue Module

# Multiprocessing Queue:-
# Multiprocessing Queue lives in shared memory
# used to share data between processes

# Queue Module:-
# Lives in-process memory
# Used to share data between threads.