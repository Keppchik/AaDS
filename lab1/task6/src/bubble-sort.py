import time
import tracemalloc
import lab1.utils as utils

tracemalloc.start()
t_start = time.perf_counter()

data = utils.read_from_file("../txtf/input.txt")
n = data[0]
a = data[1:]

for i in range(n):
    for j in range(n-1,i,-1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]

utils.write_in_file("../txtf/output.txt", a)

utils.print_time_memory(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
tracemalloc.stop()