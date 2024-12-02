import lab4.utils as utils
import os

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def add_mid(self, value):
        if len(self.queue) % 2 == 0:
            middle = len(self.queue) // 2
        else:
            middle = len(self.queue) // 2 + 1

        self.queue.insert(middle, value)

    def remove(self):
        del_value = self.queue[0]
        self.queue.pop(0)
        return del_value

    def __repr__(self):
        return f"Queue({self.queue})"

if __name__ == '__main__':
    print("LAB4 TASK 9:")
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
        elif "-" in data[i]:
            result.append(queue.remove())
        elif "*" in data[i]:
            queue.add_mid(int(data[i].split()[1]))

    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
