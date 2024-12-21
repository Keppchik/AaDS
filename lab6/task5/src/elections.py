import utils
import os


class Election:
    def __init__(self):
        self.participants = {}

    def add(self, name, value):
        if name in self.participants:
            self.participants[name] += int(value)
        else:
            self.participants[name] = int(value)

    def votes(self):
        return [f"{name} {self.participants[name]}" for name in self.participants]

if __name__ == '__main__':
    print("LAB6 TASK 5:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")

    election = Election()

    for line in data:
        line = line.split()
        election.add(line[0], line[1])

    result = election.votes()

    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)