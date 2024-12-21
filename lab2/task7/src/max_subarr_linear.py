import utils
import os

def max_subarr(arr):
    max_sub = arr[0]
    sub = arr[0]

    for i in range(1, len(arr)):
        sub = max(arr[i], sub + arr[i])
        max_sub = max(max_sub, sub)

    return max_sub

if __name__ == "__main__":
    print("LAB2 TASK 7:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    arr = data
    result = max_subarr(arr)

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, [result])
    utils.print_time_memory(time_start)