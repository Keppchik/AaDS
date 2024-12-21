import utils
import os

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def remove(self):
        if self.queue:
            value = self.queue[0]
            self.queue.pop(0)
            return value

    def __repr__(self):
        return f"Queue({self.queue})"

if __name__ == '__main__':
    print("LAB4 TASK 2:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    print(f"INPUT: {data}")
    queue = Queue()
    result = []

    for i in range(1, int(data[0])+1):
        if "+" in data[i]:
            value = int(data[i].split()[1])
            queue.add(value)
        else:
            result.append(queue.remove())

    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
