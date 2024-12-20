import lab5.utils as utils
import os

def max_heap(data, n, i):
    root = i
    if 2 * i + 1 < n and data[2 * i + 1] > data[root]:
        root = 2 * i + 1
    if 2 * i + 2 < n and data[2 * i + 2] > data[root]:
        root = 2 * i + 2

    if root != i:
        data[i], data[root] = data[root], data[i]
        max_heap(data, n, root)

def heapsort(data):
    for i in range(len(data)-1, -1, -1):
        max_heap(data, len(data), i)

    for i in range(len(data)-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        max_heap(data, i, 0)

    return data

if __name__ == '__main__':
    print("LAB4 TASK 3:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str).split()
    data = list(map(int, data))
    print(f"INPUT: {data}")

    result = heapsort(data)

    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
