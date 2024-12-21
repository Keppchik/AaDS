import unittest
import utils
from lab7.task7.src.template import check_template


class TemplateTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = "YES"

        # when
        result = check_template("k?t*n", "kitten")

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        template = "a?s*e"*200
        word = "asdce"*200
        time_start = utils.start_tracking()

        # when
        check_template(template, word)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()