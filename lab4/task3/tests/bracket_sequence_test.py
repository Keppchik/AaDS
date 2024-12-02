import random
import unittest
import lab4.utils as utils
from lab4.task3.src.bracket_sequence import isCorrect


class BracketSequenceTest(unittest.TestCase):

    def test_should_isCorrect(self):
        # given
        expected_result = ["YES", "YES", "NO", "NO", "NO"]

        # when
        data = ["()()", "([])", "([)]", "((]]", ")("]
        results = []
        for i in range(0, len(data)):
            results.append(isCorrect(data[i]))

        # then
        for i, result in enumerate(results):
            self.assertEqual(result, expected_result[i])

    def test_should_time_memory(self):
        # given
        dict = {1: "(", 2: ")", 3: "[", 4: "]"}
        data = []
        for i in range(0, 500):
            line = ""
            for i in range(0, 10 ** 4):
                value = random.randint(1, 4)
                line += dict[value]
            data.append(line)
        time_start = utils.start_tracking()

        # when
        for line in data:
            isCorrect(line)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()