import unittest
from random import randint
import lab5.utils as utils
from lab5.task3.src.network_packets import process


class NetworkPacketsTest(unittest.TestCase):

    def test_should_proccess_packets_low(self):
        # given
        array = [0, 1, 0, 0]
        expected_result = [0, -1]

        # when
        result = process(array, 1, 2)

        # then
        self.assertEqual(expected_result, result)

    def test_should_proccess_packets_big(self):
        # given
        array = [0, 2, 1, 2, 2, 2, 3, 2, 4, 2, 5, 2]
        expected_result = [0, 2, 4, 6, 8, -1]

        # when
        result = process(array, 3, 6)

        # then
        self.assertEqual(expected_result, result)

    def test_should_time_memory(self):
        # given
        array = []
        for i in range(10**5):
            array.append(i)
            array.append(randint(0, 10**6))
        time_start = utils.start_tracking()

        # when
        process(array, randint(1, 10**5), 10**5)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 10)
        self.assertLess(result[1], 512)

if __name__ == '__main__':
    unittest.main()

