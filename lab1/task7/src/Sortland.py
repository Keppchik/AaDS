import time
import tracemalloc
import lab1.utils as utils

tracemalloc.start()
t_start = time.perf_counter()

data = utils.read_from_file("../txtf/input.txt", type=float)
n = data[0]
a = data[1:]

b = a.copy()

for i in range(n):
    for j in range(n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

s = ["-1", "-1", "-1"]
for i in range(n):
    if b[i] == a[0]:
        s[0] = str(i+1)
    elif b[i] == a[n//2]:
        s[1] = str(i+1)
    elif b[i] == a[-1]:
        s[2] = str(i+1)

utils.write_in_file("../txtf/output.txt", s)

utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
tracemalloc.stop()