import time
import tracemalloc
import lab3.utils as utils
import random

def partition(arr, low, high):
    pivot = arr[low]
    j = low
    k = low
    for i in range(low + 1, high):
        if arr[i] < pivot:
            j = j + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def random_quick_sort(arr, low, high) -> list:
    if low < high:
        k = random.randint(low, high-1)
        arr[k], arr[low] = arr[low], arr[k]
        m = partition(arr, low, high)
        random_quick_sort(arr, low, m)
        random_quick_sort(arr, m + 1, high)
    return arr

def partition_three(arr, low, high):
    pivot = arr[low]
    j = low
    k = high - 1
    i = low + 1
    while i <= k:
        if arr[i] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
            i += 1
        elif arr[i] > pivot:
            arr[k], arr[i] = arr[i], arr[k]
            k -= 1
        else:
            i += 1
    return j, k

def random_quick_sort_three(arr, low, high):
    if low < high:
        k = random.randint(low, high - 1)
        arr[k], arr[low] = arr[low], arr[k]
        m1, m2 = partition_three(arr, low, high)
        random_quick_sort_three(arr, low, m1)
        random_quick_sort_three(arr, m2 + 1, high)
    return arr


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    data = utils.read_from_file("../txtf/input.txt")
    n = data[0]
    arr = data[1:]
    result = random_quick_sort_three(arr, 0, n)

    utils.write_in_file("../txtf/output.txt", result)
    utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()