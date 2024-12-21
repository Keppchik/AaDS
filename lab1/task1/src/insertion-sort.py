import os
import utils

def insertion_sort(n, a):
    for i in range(1, n):
        j = i - 1
        temp = a[i]
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp

if __name__ == '__main__':
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    a = data[1:]
    n = data[0]

    insertion_sort(n, a)

    utils.write_in_file(output_path, a)
    utils.print_time_memory(time_start)