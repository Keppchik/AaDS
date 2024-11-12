import os
import lab1.utils as utils

time_start = utils.start_tracking()
input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

data = utils.read_from_file(input_path)
a = data[:-1]
v = data[-1]

k = []
for i in range(len(a)):
    if a[i] == v:
        k.append(i)

path = output_path
if len(k) == 0:
    utils.write_in_file(path, [-1])
elif len(k) == 1:
    utils.write_in_file(path, k)
else:
    arr = ' '.join(map(str, k))
    utils.write_in_file(path, str(len(k))+'\n'+ arr, split_str="")

utils.print_time_memory(time_start)