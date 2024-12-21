import unittest
import utils
from lab1.task9.src.adding_binary_numbers import adding_binary_numbers


class AddingBinaryNumbersTest(unittest.TestCase):

    def test_should_example(self):
        # given
        number1 = "1111"
        number2 = "1111"
        expected_result = [1,1,1,1,0]

        # when
        result = adding_binary_numbers(number1, number2)

        # then
        self.assertEqual(expected_result, result)

    def test_should_time_memory(self):
        # given
        number1 = "1" * 10**3
        number2 = "1" * 10**3
        time_start = utils.start_tracking()

        # when
        adding_binary_numbers(number1, number2)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)

if __name__ == '__main__':
    unittest.main()

