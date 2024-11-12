import os
import lab1.utils as utils

time_start = utils.start_tracking()
input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

data = utils.read_from_file(input_path, type=str)
s1, s2 = data.split()
s3 = [0] + [int(s1[i]) + int(s2[i]) for i in range(len(s1))]

for i in range(len(s3)-1, 0, -1):
    if s3[i] >= 2:
        s3[i] -= 2
        s3[i-1] += 1

utils.write_in_file(output_path, s3, split_str="")
utils.print_time_memory(time_start)