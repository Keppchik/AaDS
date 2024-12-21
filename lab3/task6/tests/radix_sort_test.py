import unittest
from lab3.task6.src.radix_sort import radix_sort

class RadixSortTest(unittest.TestCase):

    def test_should_radix_sort(self):
        expected_result = 51
        data = [[7,1,4,9],[2,7,8,11]]
        data = [data[0][i]*data[1][j] for i in range(len(data[0])) for j in range(len(data[1]))]

        array = radix_sort(data, len(data))
        result = 0
        for i in range(0, len(data), 10):
            result += array[i]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()