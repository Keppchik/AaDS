import lab3.task1.src.quick_sort as QS
import utils
import math
import os

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def perebor(points, low, high):
    min_dis = float('inf')
    for i in range(low, high):
        for j in range(i+1, high):
            min_dis = min(distance(points[i], points[j]), min_dis)
    return min_dis

def closest_points(points, low, high):
    if high - low <= 3:
        return perebor(points, low, high)
    else:
        mid = (low + high) // 2
        d_left = closest_points(points, low, mid)
        d_right = closest_points(points, mid, high)
        d_lr = min(d_left, d_right)

        near_line = []
        for i in range(low, high):
            if abs(points[i][0] - points[mid][0]) < d_lr:
                near_line.append(points[i])
        d = min(d_lr, perebor(near_line, 0, len(near_line)))

        return d


if __name__ == "__main__":
    print("LAB3 TASK 9:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    f = open(input_path, "r")
    n = int(f.readline())
    points = []
    for _ in range(n):
        line = tuple(map(int, f.readline().split()))
        points.append(line)
    points = QS.random_quick_sort_three(points, 0, n)

    result = f"{closest_points(points, 0, n):.6}"

    print(f"INPUT: {points}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, [result])
    utils.print_time_memory(time_start)