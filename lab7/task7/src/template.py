import utils
import os

def check_template(template, word):
    n, m = len(template), len(word)
    matrix = [[False] * (m + 1) for _ in range(n + 1)]
    matrix[0][0] = True

    for i in range(1, n + 1):
        if template[i - 1] == '*':
            matrix[i][0] = matrix[i - 1][0]
        else:
            break

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if template[i - 1] == '*':
                matrix[i][j] = matrix[i - 1][j] or matrix[i][j - 1]
            elif template[i - 1] == '?' or template[i - 1] == word[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]

    return "YES" if matrix[n][m] else "NO"

if __name__ == '__main__':
    print("LAB7 TASK 7:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split('\n')

    result = check_template(data[0], data[1])

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, [result], split_str="\n")
    utils.print_time_memory(time_start)

