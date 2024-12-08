import os
import lab1.utils as utils

time_start = utils.start_tracking()
input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

data = utils.read_from_file(input_path, type=float)
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

utils.write_in_file(output_path, s)
utils.print_time_memory(time_start)