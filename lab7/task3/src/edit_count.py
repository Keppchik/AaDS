import utils
import os

def edit_count(word1, word2):
    n, m = len(word1), len(word2)
    matrix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        matrix[i][0] = i
    for j in range(m + 1):
        matrix[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])

    return matrix[n][m]

if __name__ == '__main__':
    print("LAB7 TASK 3:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    word1, word2 = data.split()

    result = edit_count(word1, word2)

    print(f"INPUT: {data.split()}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, [result], split_str="\n")
    utils.print_time_memory(time_start)

