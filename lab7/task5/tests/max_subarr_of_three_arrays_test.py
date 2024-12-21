import unittest
import utils
from lab7.task5.src.max_subarr_of_three_arrays import max_subarr


class MaxSubArrTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = 3

        # when
        result = max_subarr([8, 3, 2, 1, 7],[8, 2, 1, 3, 8, 10, 7],[6, 8, 3, 1, 4, 7])

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        array1 = [i for i in range(100)]
        array2 = [i for i in range(100)]
        array3 = [i for i in range(100)]
        time_start = utils.start_tracking()

        # when
        max_subarr(array1, array2, array3)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 1)


if __name__ == '__main__':
    unittest.main()