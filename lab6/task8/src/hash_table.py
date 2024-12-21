import lab6.utils as utils
import os

def make_table(n, x, a, b, ac, bc, ad, bd):
    table = set()
    for i in range(n):
        if x in table:
            a = (a + ac) % 10**3
            b = (b + bc) % 10**15
        else:
            a = (a + ad) % 10**3
            b = (b + bd) % 10**15
            table.add(x)
        x = (x * a + b) % 10**15
    return x, a, b

if __name__ == '__main__':
    print("LAB6 TASK 8:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split()
    data = list(map(int, data))

    result = make_table(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str=" ")
    utils.print_time_memory(time_start)