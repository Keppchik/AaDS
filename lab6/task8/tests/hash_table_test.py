import unittest
from random import randint
import utils
from lab6.task8.src.hash_table import make_table


class HashTableTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = (3, 1, 1)

        # when
        result = make_table(4, 0,0,0,1,1,0,0)

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        make_table(10**6, randint(1, 10**15), randint(1, 10**3), randint(1, 10**15), randint(1, 10**3),randint(1, 10**15), randint(1, 10**3), randint(1, 10**15))
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 5)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()