import time
import tracemalloc
import lab2.utils as utils

if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    data = utils.read_from_file("../txtf/input.txt")
    a = data

    pref = [0]*(len(a)+1)
    for i in range(1, len(a)+1):
        pref[i] = pref[i-1] + a[i-1]

    min_l = [float('inf')]*(len(a))
    min_l[0] = 0
    for i in range(1,len(a)):
        min_l[i] = min(pref[i], min_l[i-1])

    max_arr = float('-inf')
    for i in range(1, len(a)+1):
        max_arr = max(max_arr, pref[i] - min_l[i-1])

    utils.write_in_file("../txtf/output.txt", [max_arr])
    utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()