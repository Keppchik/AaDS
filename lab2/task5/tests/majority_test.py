import unittest
from lab2.task5.src.majority import majority

class MajorityTest(unittest.TestCase):

    def test_should_majority1(self):
        expected_result = 1
        data = [2,3,9,2,2]
        data.sort()

        result = majority(data, len(data))

        self.assertEqual(result, expected_result)

    def test_should_majority2(self):
        expected_result = 0
        data = [1,2,3,4,5]
        data.sort()

        result = majority(data, len(data))

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()