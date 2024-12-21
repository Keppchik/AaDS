import utils
import os

def min_coins(money, coins):
    result = [float('inf')] * (money + 1)
    result[0] = 0

    for coin in coins:
        for i in range(coin, money + 1):
            result[i] = min(result[i], result[i - coin] + 1)

    if result[money] == float('inf'):
        return -1
    else:
        return result[money]

if __name__ == '__main__':
    print("LAB7 TASK 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split()
    data = list(map(int, data))

    result = min_coins(data[0], data[2:])

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, [result], split_str="\n")
    utils.print_time_memory(time_start)
