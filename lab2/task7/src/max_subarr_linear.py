import time
import tracemalloc
import lab2.utils as utils

if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    data = utils.read_from_file("../txtf/input.txt")
    a = data

    max_sub = a[0]
    sub = a[0]

    for i in range(1, len(a)):
        sub = max(a[i], sub + a[i])
        max_sub = max(max_sub, sub)

    utils.write_in_file("../txtf/output.txt", [max_sub])
    utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()