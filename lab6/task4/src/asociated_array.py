import lab6.utils as utils
import os
from collections import OrderedDict

class AsociatedArray:
    def __init__(self):
        self.dict = OrderedDict()

    def put(self, key, value):
        self.dict[key] = value

    def get(self, key):
        return self.dict.get(key, "<none>")

    def delete(self, key):
        self.dict.pop(key, "<none>")

    def prev(self, key):
        if key not in self.dict:
            return "<none>"
        keys = list(self.dict.keys())
        index = keys.index(key)
        return self.dict[keys[index - 1]] if index > 0 else "<none>"

    def next(self, key):
        if key not in self.dict:
            return "<none>"
        keys = list(self.dict.keys())
        index = keys.index(key)
        return self.dict[keys[index + 1]] if index < len(keys) - 1 else "<none>"

if __name__ == '__main__':
    print("LAB6 TASK 4:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")

    asociated_array = AsociatedArray()
    result = []

    for i in range(1, int(data[0])+1):
        line = data[i].split(" ")
        if "next" in data[i]:
            key = line[1]
            result.append(asociated_array.next(key))
        elif "prev" in data[i]:
            key = line[1]
            result.append(asociated_array.prev(key))
        elif "put" in data[i]:
            key, value = line[1], line[2]
            asociated_array.put(key, value)
        elif "delete" in data[i]:
            key = line[1]
            asociated_array.delete(key)
        elif "get" in data[i]:
            key = line[1]
            result.append(asociated_array.get(key))

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)