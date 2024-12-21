import unittest
from lab3.task3.src.pugalo_sort import can_be_sorted

class PugaloSortTest(unittest.TestCase):

    def test_should_pugalo_sort(self):
        expected_result = "НЕТ"
        data = [2,1,3]
        result = can_be_sorted(data, 3, 4)
        self.assertEqual(result, expected_result)

    def test_should_not_pugalo_sort(self):
        expected_result = "ДА"
        data = [1,5,3,4,1]
        result = can_be_sorted(data,5, 3)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()