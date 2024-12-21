import unittest
import utils
import random
from lab4.task6.src.queue_minimum import Queue


class QueueMinimumTest(unittest.TestCase):

    def test_should_minimum(self):
        # given
        expected_result = [1, 1, 10]

        # when
        result = []
        queue = Queue()
        queue.add(1)
        result.append(queue.min())
        queue.add(10)
        result.append(queue.min())
        queue.remove()
        result.append(queue.min())

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        queue = Queue()
        for i in range(10**5):
            value = random.randint(1, 10**6)
            queue.add(value)
            queue.min()
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()