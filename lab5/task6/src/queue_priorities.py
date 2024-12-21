import utils
import os

class Queue:
    def __init__(self):
        self.queue = []
        self.int_add = 1
        self.minimum = float("+inf")

    def add(self, value):
        self.queue.append((value, self.int_add))
        self.int_add += 1

    def remove_min(self):
        if len(self.queue) == 0:
            return "*"
        index = self.queue.index(min(self.queue))
        return self.queue.pop(index)[0]

    def replace(self, when_add, value):
        for i in range(len(self.queue)):
            if self.queue[i][1] == when_add:
                self.queue[i] = (value, when_add)

    def __repr__(self):
        return f"Queue({self.queue})"

def main(data):
    queue = Queue()
    result = []

    for line in data:
        line = line.split()
        if line[0] == "A":
            queue.add(int(line[1]))
        elif line[0] == "X":
            result.append(queue.remove_min())
        elif line[0] == "D":
            queue.replace(int(line[1]), int(line[2]))

    return result

if __name__ == '__main__':
    print("LAB5 TASK 6:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    print(f"INPUT: {data}")

    result = main(data)

    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
