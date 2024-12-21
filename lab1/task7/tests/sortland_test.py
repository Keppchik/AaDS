import unittest
import utils
from lab1.task7.src.Sortland import sortland


class SortlandtTest(unittest.TestCase):

    def test_should_example(self):
        # given
        array = [10.00, 8.70, 0.01, 5.00, 3.00]
        expected_result = ["3", "4", "1"]

        # when
        result = sortland(5, array)

        # then
        self.assertEqual(expected_result, result)

    def test_should_time_memory(self):
        # given
        array = [x for x in range(9999)]
        time_start = utils.start_tracking()

        # when
        sortland(9999, array)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)

if __name__ == '__main__':
    unittest.main()

