import time
from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    t = time.time()
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    print('total time:', time.time() - t)
    print('without Pool----->')
    print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print('total time:', time.time() - t)