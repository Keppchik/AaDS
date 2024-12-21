import unittest
import utils
from lab4.task2.src.queue import Queue


class QueueTest(unittest.TestCase):

    def test_should_remove(self):
        # given
        expected_result = 1

        # when
        queue = Queue()
        queue.add(1)
        queue.add(2)
        result = queue.remove()

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        queue = Queue()
        for i in range(10**6):
            queue.add(i)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()