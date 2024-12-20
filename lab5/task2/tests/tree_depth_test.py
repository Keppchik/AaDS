import unittest
import lab5.utils as utils
from lab5.task2.src.tree_depth import tree_depth

class TreeDepthTest(unittest.TestCase):

    def test_should_return_tree_depth_first_exampl(self):
        # given
        array = [4, -1, 4, 1, 1]
        expected_result = 3

        # when
        result = tree_depth(len(array), array)

        # then
        self.assertEqual(expected_result, result)

    def test_should_return_tree_depth_second_example(self):
        # given
        array = [-1, 0, 4, 0, 3]
        expected_result = 4

        # when
        result = tree_depth(len(array), array)

        # then
        self.assertEqual(expected_result, result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()
        array = [i-1 for i in range(10**5)]

        # when
        tree_depth(len(array), array)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 3)
        self.assertLess(result[1], 512)

if __name__ == '__main__':
    unittest.main()

