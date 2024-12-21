import utils
import os

def max_subarr(array1, array2, array3):
    n, m, l = len(array1), len(array2), len(array3)
    matrix = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if array1[i - 1] == array2[j - 1] == array3[k - 1]:
                    matrix[i][j][k] = matrix[i-1][j-1][k-1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j-1][k], matrix[i][j][k-1])

    return matrix[n][m][l]

if __name__ == '__main__':
    print("LAB7 TASK 5:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split()
    n = int(data[0])
    m = int(data[n+1])
    l = int(data[n+m+2])
    array1 = data[1:n+1]
    array2 = data[n+2:n+m+2]
    array3 = data[n+m+3:]

    result = max_subarr(array1, array2, array3)

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, [result], split_str="\n")
    utils.print_time_memory(time_start)

