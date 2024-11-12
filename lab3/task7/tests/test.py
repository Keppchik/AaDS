import unittest
from lab3.task7.src.letter_sort import letter_sort

class LetterSortTest(unittest.TestCase):

    def test_should_letter_sort1(self):
        expected_result = [2, 3, 1]
        data = ["bab", "bba", "baa"]
        result = letter_sort(data, 3, 3, 1)
        self.assertEqual(result, expected_result)

    def test_should_letter_sort2(self):
        expected_result = [3,1,2]
        data = ["bab", "bba", "baa"]
        result = letter_sort(data, 3, 3, 2)
        self.assertEqual(result, expected_result)

    def test_should_letter_sort3(self):
        expected_result = [3,1,2]
        data = ["bab", "bba", "baa"]
        result = letter_sort(data, 3, 3, 2)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()