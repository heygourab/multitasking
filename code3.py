from multiprocessing import Process, Value
# we use Value for shared memory


def calc_square(arr, value):
    for element in arr:
        value.value += element
    print(f'inside total value: {value.value}')


if __name__ == '__main__':
    value = Value('i', 0)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    p = Process(target=calc_square, args=(arr, value))
    p.start()
    p.join()
    print(f'outside total value: {value.value}')