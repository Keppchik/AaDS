import time
import tracemalloc
import lab2.utils as utils

def merge(A, p, q, r):
    L = A[p:q]
    R = A[q:r]
    R.append(float('inf'))
    L.append(float('inf'))

    i, j = 0, 0
    for k in range(p, r):
        if L[i] <= R[j] :
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r - 1:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)
    return A

def majority(arr, n):
    cur_max = 0
    cur = 1
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            cur += 1
        else:
            cur_max = max(cur_max, cur)
            cur = 1

    if cur_max >= n/2:
        return 1
    return 0

if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    data = utils.read_from_file("../txtf/input.txt")
    n = data[0]
    arr = data[1:]

    merge_sort(arr, 0, n)

    result = majority(arr, n)

    utils.write_in_file("../txtf/output.txt", [result])
    utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()