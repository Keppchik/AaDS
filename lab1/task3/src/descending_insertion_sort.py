import utils
import os

time_start = utils.start_tracking()
input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

data = utils.read_from_file(input_path)
n = data[0]
a = data[1:]

for i in range(1, n):
    j = i-1
    temp = a[i]
    while j >= 0 and temp > a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = temp

utils.write_in_file(output_path, a)
utils.print_time_memory(time_start)