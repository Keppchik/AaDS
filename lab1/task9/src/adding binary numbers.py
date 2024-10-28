import time
import tracemalloc
import lab1.utils as utils

tracemalloc.start()
t_start = time.perf_counter()

data = utils.read_from_file("../txtf/input.txt", type=str)
s1, s2 = data.split()
s3 = [0] + [int(s1[i]) + int(s2[i]) for i in range(len(s1))]

for i in range(len(s3)-1, 0, -1):
    if s3[i] >= 2:
        s3[i] -= 2
        s3[i-1] += 1

utils.write_in_file("../txtf/output.txt", s3, split_str="")

utils.time_memory_usage(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
tracemalloc.stop()