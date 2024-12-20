import lab6.utils as utils
import os

class Set:
    def __init__(self):
        self.data = set()

    def add(self,value):
        if value not in self.data:
            self.data.add(value)

    def remove(self,value):
        self.data.discard(value)

    def in_set(self,value):
        if value in self.data:
            return "Y"
        else:
            return "N"

if __name__ == '__main__':
    print("LAB6 TASK 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    set = Set()
    result = []

    for i in range(1, int(data[0])+1):
        if "A" in data[i]:
            value = int(data[i].split()[1])
            set.add(value)
        elif "D" in data[i]:
            value = int(data[i].split()[1])
            set.remove(value)
        elif "?" in data[i]:
            value = int(data[i].split()[1])
            result.append(set.in_set(value))

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)

