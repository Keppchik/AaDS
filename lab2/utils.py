import random
import time
import tracemalloc

def read_from_file(filename: str, type = int):
    f = open(filename, "r")
    if type == float:
        data = [int(f.readline())] + [float(x) for x in f.readline().split()]
        return data
    elif type == str:
        data = f.read()
        return data
    data = list(map(int, f.read().split()))
    return data

def write_in_file(filename: str, array: any, split_str: str = ' ') -> None:
    with open(filename, 'w') as f:
        f.write(split_str.join(map(str,array)))
    return None

def start_tracking():
    tracemalloc.start()
    return time.perf_counter()

def print_time_memory(time_start):
    print(f'Время работы: {time.perf_counter() - time_start} секунд ')
    print(f'Память: {tracemalloc.get_traced_memory()[1] / (1024 ** 2)} МБ')
    tracemalloc.stop()


def random_array(n: int, values: int = 10**4) -> list:
    arr = []
    for _ in range(n):
        arr.append(random.randint(-1*values, values))
    return arr

def worst_array(n: int) -> list:
    arr = []
    for i in range(n,0,-1):
        arr.append(i)
    return arr

def best_array(n: int) -> list:
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

def is_sorted(arr: list) -> bool:
    for i in range(1, len(arr)-1):
        if arr[i-1] > arr[i]:
            return False
    return True