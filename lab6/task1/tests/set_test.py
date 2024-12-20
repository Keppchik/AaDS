import unittest
import lab6.utils as utils
from lab6.task1.src.set import Set


class SetTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = ["Y", "N", "N"]

        # when
        result = []
        set = Set()
        set.add(2)
        set.add(5)
        set.add(3)
        result.append(set.in_set(2))
        result.append(set.in_set(4))
        set.add(2)
        set.remove(2)
        result.append(set.in_set(2))

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        set = Set()
        for i in range(5 * 10**5):
            set.add(i)
            set.in_set(i)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()