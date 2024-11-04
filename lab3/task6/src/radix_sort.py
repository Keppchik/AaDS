import time
import tracemalloc
import lab3.utils as utils


def counting_sort(arr, r, n):
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // r) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n-1, -1, -1):
        index = (arr[i] // r) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr, n):
    max_num = max(arr)
    r = 1
    while max_num // r > 0:
        counting_sort(arr, r, n)
        r = r * 10
    return arr


if __name__ == "__main__":
    data = utils.read_from_file("../txtf/input.txt")
    n, m = data[0], data[1]
    arr1 = data[2:n+2]
    arr2 = data[n+2:]
    arr3 = [x*y for x in arr1 for y in arr2]

    tracemalloc.start()
    t_start = time.perf_counter()

    sorted_arr = radix_sort(arr3, n*m)

    result = 0
    for i in range(0, n*m, 10):
        result += sorted_arr[i]

    utils.write_in_file("../txtf/output.txt", [result])
    utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()