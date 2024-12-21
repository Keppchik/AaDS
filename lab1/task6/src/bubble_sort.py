import os
import utils

def bubble_sort(n, a):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]

if __name__ == '__main__':
    print("LAB1 TASK 6:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = data[0]
    a = data[1:]

    bubble_sort(n, a)

    print(f"INPUT: {data}")
    print(f"RESULT: {a}")

    utils.write_in_file(output_path, a)
    utils.print_time_memory(time_start)