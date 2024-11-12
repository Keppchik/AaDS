import time
import tracemalloc
import lab1.utils as utils

tracemalloc.start()
t_start = time.perf_counter()

data = utils.read_from_file("../txtf/input.txt")
a = data[:-1]
v = data[-1]

k = []
for i in range(len(a)):
    if a[i] == v:
        k.append(i)

path = "../txtf/output.txt"
if len(k) == 0:
    utils.write_in_file(path, [-1])
elif len(k) == 1:
    utils.write_in_file(path, k)
else:
    arr = ' '.join(map(str, k))
    utils.write_in_file(path, str(len(k))+'\n'+ arr, split_str="")

utils.print_time_memory(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
tracemalloc.stop()