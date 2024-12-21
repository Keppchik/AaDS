import utils
import os

def index_hirsh(arr):
    count = [0] * (max(arr)+1)
    for i in range(0, len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)-2, -1, -1):
        count[i] += count[i+1]

    for i in range(len(count)-1, -1, -1):
        if count[i] >= i:
            return i


if __name__ == "__main__":
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    arr = data
    result = index_hirsh(arr)

    utils.write_in_file(output_path, [result])
    utils.print_time_memory(time_start)