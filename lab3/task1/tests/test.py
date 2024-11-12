import unittest
from lab3.task1.src.quick_sort import *
from lab3.utils import *

class QuickSortTest(unittest.TestCase):

    def test_should_quick_sort(self):
        expected_result = [n for n in range(1, 10**4+1)]
        data = worst_array(10**4)

        result = random_quick_sort_three(data, 0, len(data))

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()