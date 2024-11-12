import lab2.utils as utils
import os

def bin_search(a, value, p, r):
    if p < r:
        q = (p + r) // 2
        if value < a[q]:
            return bin_search(a, value, p, q)
        elif value > a[q]:
            return bin_search(a, value, q + 1, r)
        else:
            return q
    return -1


if __name__ == "__main__":
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = data[0]
    a = data[1:n+1]
    k = data[n+1]
    b = data[n+2:]

    result = [bin_search(a, number, 0, n) for number in b]

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)