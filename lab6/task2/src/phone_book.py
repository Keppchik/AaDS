import utils
import os

class PhoneBook:
    def __init__(self):
        self.dict = {}

    def add(self, phone, name):
        self.dict[phone] = name

    def find(self, phone):
        return self.dict.get(phone, "not found")

    def delete(self, phone):
        self.dict.pop(phone, None)


if __name__ == '__main__':
    print("LAB6 TASK 2:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")

    phone_book = PhoneBook()
    result = []

    for i in range(1, int(data[0])+1):
        line = data[i].split(" ")
        if "add" in data[i]:
            phone, name = line[1], line[2]
            phone_book.add(phone, name)
        elif "del" in data[i]:
            phone = line[1]
            phone_book.delete(phone)
        elif "find" in data[i]:
            phone = line[1]
            result.append(phone_book.find(phone))


    print(f"INPUT: {data}")
    print(f"RESULT: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)