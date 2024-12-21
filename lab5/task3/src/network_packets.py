import utils
import os

def process(data, s, n):
    packages = []
    for i in range(0, n*2, 2):
        packages.append((data[i], data[i+1]))

    queue = []
    result = []

    for package in packages:
        if len(queue) < s:
            if queue:
                time_start = max(queue[-1][1], package[0])
            else:
                time_start = package[0]
            queue.append((time_start, time_start + package[1]))
            result.append(time_start)
        elif queue[0][1] <= package[0]:
            queue.pop(0)
            if queue:
                time_start = max(queue[-1][1], package[0])
            else:
                time_start = package[0]
            queue.append((time_start, time_start + package[1]))
            result.append(time_start)
        else:
            result.append(-1)

    return result


if __name__ == '__main__':
    print("LAB5 TASK 3:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str).split()
    data = list(map(int, data))
    result = process(data[2:], data[0], data[1])

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
