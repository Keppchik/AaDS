import utils
import random
import os

def partition(arr, low, high):
    pivot = arr[low]
    j = low
    for i in range(low + 1, high):
        if arr[i] < pivot:
            j = j + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def random_quick_sort(arr, low, high) -> list:
    if low < high:
        k = random.randint(low, high-1)
        arr[k], arr[low] = arr[low], arr[k]
        m = partition(arr, low, high)
        random_quick_sort(arr, low, m)
        random_quick_sort(arr, m + 1, high)
    return arr

def partition_three(arr, low, high):
    pivot = arr[low]
    j = low
    k = high - 1
    i = low + 1
    while i <= k:
        if arr[i] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
            i += 1
        elif arr[i] > pivot:
            arr[k], arr[i] = arr[i], arr[k]
            k -= 1
        else:
            i += 1
    return j, k

def random_quick_sort_three(arr, low, high):
    if low < high:
        k = random.randint(low, high - 1)
        arr[k], arr[low] = arr[low], arr[k]
        m1, m2 = partition_three(arr, low, high)
        random_quick_sort_three(arr, low, m1)
        random_quick_sort_three(arr, m2 + 1, high)
    return arr


if __name__ == "__main__":
    print("LAB3 TASK 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = data[0]
    arr = data[1:]
    result = random_quick_sort_three(arr, 0, n)

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)