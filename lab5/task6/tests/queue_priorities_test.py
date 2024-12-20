import unittest
import lab5.utils as utils
from lab5.task6.src.queue_priorities import main, Queue


class QueueTest(unittest.TestCase):

    def test_should_remove_min(self):
        # given
        expected_result = 1

        # when
        queue = Queue()
        queue.add(2)
        queue.add(1)
        queue.add(2)
        result = queue.remove_min()

        # then
        self.assertEqual(result, expected_result)

    def test_should_example(self):
        # given
        data = ['8', 'A 3', 'A 4', 'A 2', 'X', 'D 2 1', 'X', 'X', 'X']
        expected_result = [2, 1, 3, '*']

        # when
        result = main(data)

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