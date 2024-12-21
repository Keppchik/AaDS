import utils
import os

def maxsubarray(arr):
    pref = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        pref[i] = pref[i - 1] + arr[i - 1]

    min_l = [float('inf')] * (len(arr))
    min_l[0] = 0
    for i in range(1, len(arr)):
        min_l[i] = min(pref[i], min_l[i - 1])

    max_arr = float('-inf')
    for i in range(1, len(arr) + 1):
        max_arr = max(max_arr, pref[i] - min_l[i - 1])

    return max_arr

if __name__ == "__main__":
    print("LAB2 TASK 6:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    arr = data
    result = maxsubarray(arr)

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, [result])
    utils.print_time_memory(time_start)