import unittest
import utils
from lab1.task3.src.descending_insertion_sort import descending_insertion_sort

class DescendingInsertionSortTest(unittest.TestCase):

    def test_should_example(self):
        # given
        array = [1,2,3,4,5,6,7,8,9,10]
        expected_result = [10,9,8,7,6,5,4,3,2,1]

        # when
        descending_insertion_sort(10, array)

        # then
        self.assertEqual(expected_result, array)

    def test_should_time_memory(self):
        # given
        array = [x for x in range(10**3)]
        time_start = utils.start_tracking()

        # when
        descending_insertion_sort(10**3, array)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)

if __name__ == '__main__':
    unittest.main()

