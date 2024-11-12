import unittest
from lab2.task6.src.find_max_profit import maxsubarray

class MaxProfitTest(unittest.TestCase):

    def test_should_max_profit(self):
        expected_result = 8
        data = [3,-4,-5,8,-2,-7]

        result = maxsubarray(data)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()