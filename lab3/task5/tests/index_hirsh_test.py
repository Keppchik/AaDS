import unittest
from lab3.task5.src.index_hirsh import index_hirsh

class IndexHirshTest(unittest.TestCase):

    def test_should_index_hirsh1(self):
        expected_result = 3
        data = [3,0,6,1,5]
        result = index_hirsh(data)
        self.assertEqual(result, expected_result)

    def test_should_index_hirsh2(self):
        expected_result = 1
        data = [1,3,1]
        result = index_hirsh(data)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()