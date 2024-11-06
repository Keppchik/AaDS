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

def print_time_memory(time, memory):
    print(f'Время работы: {time} секунд ')
    print(f'Память: {memory} МБ')