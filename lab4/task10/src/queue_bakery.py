import lab4.utils as utils
import os

class Person:
    def __init__(self, time, scale, persons):
        self.time = time
        self.scale = scale
        self.end_time = self.calc_end_time(persons)

    def calc_end_time(self, persons):
        k = 0
        max_end_time = -1
        for person in persons:
            if person.end_time > self.time:
                max_end_time = max(person.end_time, max_end_time)
                k += 1

        if k > self.scale:
            return self.time
        else:
            return max_end_time + 10 if max_end_time > -1 else self.time + 10


if __name__ == '__main__':
    print("LAB4 TASK 10:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    print(f"INPUT: {data}")
    data = data[1:]
    persons = []
    result = []
    for line in data:
        line = line.split()
        persons.append(Person(int(line[0]) * 60 + int(line[1]), int(line[2]), persons))
        end_time = f"{persons[-1].end_time // 60} {persons[-1].end_time % 60}"
        result.append(end_time)

    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
