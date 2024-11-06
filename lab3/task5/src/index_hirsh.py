import time
import tracemalloc
import lab3.utils as utils

def index_hirsh(arr):
    count = [0] * (max(arr)+1)
    for i in range(0, len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)-2, -1, -1):
        count[i] += count[i+1]

    for i in range(len(count)-1, -1, -1):
        if count[i] >= i:
            return i


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    data = utils.read_from_file("../txtf/input.txt")
    arr = data
    result = index_hirsh(arr)

    utils.write_in_file("../txtf/output.txt", [result])
    utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()