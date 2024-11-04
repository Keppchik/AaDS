import random

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

def time_memory_usage(time, memory):
    print(f'Время работы: {time} секунд ')
    print(f'Память: {memory} МБ')

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
        if arr[i] >= arr[i-1]:
            pass
        else:
            return False
    return True