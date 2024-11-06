import time
import tracemalloc
import lab3.utils as utils
import random

def razbiyenie(arr,n, k):
    lists = [[] for _ in range(k)]
    for i in range(n):
        lists[i%k].append(arr[i])
    return lists

def partition(arr, low, high):
    pivot = arr[low]
    j = low
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

def sort_lists(lists):
    for i in range(len(lists)):
        lists[i] = random_quick_sort(lists[i], 0, len(lists[i]))

def pugalo_sort(arr, n, k):
    lists = razbiyenie(arr, n, k)
    sort_lists(lists)

    result = []
    j = -1
    for i in range(n):
        if i % k == 0:
            j = j + 1
        result.append(lists[i%k][j])

    return result

def can_be_sorted(arr, n, k):
    arr = pugalo_sort(arr, n, k)

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return "НЕТ"
    return "ДА"


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    data = utils.read_from_file("../txtf/input.txt")
    n = data[0]
    k = data[1]
    arr = data[2:]
    result = can_be_sorted(arr, n, k)

    utils.write_in_file("../txtf/output.txt", [result])
    utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()