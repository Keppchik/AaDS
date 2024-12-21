import unittest
import utils
from lab7.task3.src.edit_count import edit_count


class EditCountTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = 3

        # when
        result = edit_count("short","ports")

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        word1 = "s" * 1000
        word2 = "p" * 1000
        time_start = utils.start_tracking()

        # when
        edit_count(word1, word2)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()