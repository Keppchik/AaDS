import time
import tracemalloc
import lab1.utils as utils

tracemalloc.start()
t_start = time.perf_counter()

data = utils.read_from_file("../txtf/input.txt")
n = data[0]
a = data[1:]

for i in range(1, n):
    j = i-1
    temp = a[i]
    while j >= 0 and temp < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = temp


utils.write_in_file("../txtf/output.txt", a)
utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
tracemalloc.stop()