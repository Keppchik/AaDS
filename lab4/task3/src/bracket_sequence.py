import lab4.utils as utils
import os

def isCorrect(line):
    while "[]" in line or "()" in line:
        line = line.replace("[]", "")
        line = line.replace("()", "")
    if line == "":
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    data = data[1:]
    result = []

    for line in data:
        result.append(isCorrect(line))

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)