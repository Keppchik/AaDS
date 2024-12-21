import os
import utils

def linear_search(a, target):
    k = []
    for i in range(len(a)):
        if a[i] == target:
            k.append(i)
    return k

if __name__ == '__main__':
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    a = data[:-1]
    v = data[-1]

    k = linear_search(a, v)

    if len(k) == 0:
        utils.write_in_file(output_path, [-1])
    elif len(k) == 1:
        utils.write_in_file(output_path, k)
    else:
        arr = ' '.join(map(str, k))
        utils.write_in_file(output_path, str(len(k))+'\n'+ arr, split_str="")

    utils.print_time_memory(time_start)