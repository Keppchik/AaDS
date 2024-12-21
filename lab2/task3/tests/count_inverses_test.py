import unittest
from lab2.task3.src.count_inverses import main

class CountInversesTest(unittest.TestCase):

    def test_should_count_inverses(self):
        expected_result = 17
        data = [1,8,2,1,4,7,3,2,3,6]

        result = main(True, data, 10)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()