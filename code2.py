# Q.Sharing Data Between Processes Using Array and Value?
from multiprocessing import Process, Array
# we use Array type shared memory


def calc_square(numbers, result):
    for idx, number in enumerate(numbers):
        result[idx] = number**2
    print(f'inside process: {result[:]}')


if __name__ == '__main__':
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = Array('i', len(numbers))  # this object for shared memory
    p = Process(target=calc_square, args=(numbers, result))
    p.start()
    p.join()
    print(f'outside Process: {result[:]}')

# array_object[:] --> [:] this is way to print all the element in this array object.