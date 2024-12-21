import unittest
import utils
import random
from lab4.task10.src.queue_bakery import Person


class QueueBakeryTest(unittest.TestCase):

    def test_should_end_time(self):
        # given
        expected_result = ['13 10', '14 10', '14 1', '14 20', '14 3']
        persons = []
        lines = ['13 0 100', '14 0 0', '14 1 0', '14 2 3', '14 3 0']
        for line in lines:
            line = line.split()
            persons.append(Person(int(line[0]) * 60 + int(line[1]), int(line[2]), persons))

        # when
        result = []
        for i in range(len(persons)):
            end_time = f"{persons[i].end_time // 60} {persons[i].end_time % 60}"
            result.append(end_time)

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        persons = []
        for i in range(100):
            time = random.randint(0,60) * 60 + random.randint(0,60)
            persons.append(Person(time, random.randint(0, 100), persons))
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()