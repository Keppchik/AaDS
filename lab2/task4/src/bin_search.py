import time
import tracemalloc
import lab2.utils as utils

def bin_search(a, value, p, r):
    if p < r:
        q = (p + r) // 2
        if value < a[q]:
            return bin_search(a, value, p, q)
        elif value > a[q]:
            return bin_search(a, value, q + 1, r)
        else:
            return q
    return -1


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    data = utils.read_from_file("../txtf/input.txt")
    n = data[0]
    a = data[1:n+1]
    k = data[n+1]
    b = data[n+2:]

    result = [bin_search(a, number, 0, n) for number in b]

    utils.write_in_file("../txtf/output.txt", result)
    utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()