import lab5.utils as utils
import os
from collections import deque


def bfs(root, tree):
    queue = deque([(root, 1)])
    max_height = 1

    while queue:
        node, depth = queue.popleft()
        max_height = max(max_height, depth)
        for leaf in tree[node]:
            queue.append((leaf, depth + 1))

    return max_height

def tree_depth(n, array):
    tree = [[] for i in range(n)]
    root = -1

    for i in range(n):
        if array[i] == -1:
            root = i
        else:
            tree[array[i]].append(i)

    return bfs(root, tree)

def main(data, n):
    n = int(n)
    array = list(map(int, data[:n]))
    return tree_depth(n, array)

if __name__ == '__main__':
    print("LAB5 TASK 2:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str).split()
    result = [main(data[1:], data[0])]

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
