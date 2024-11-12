import unittest
from lab2.task7.src.max_subarr_linear import max_subarr

class MaxSubarrayTest(unittest.TestCase):

    def test_should_max_subarray(self):
        expected_result = 13
        data = [7,-5,8,3,-6,-8,5,2,-6,9]

        result = max_subarr(data)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()