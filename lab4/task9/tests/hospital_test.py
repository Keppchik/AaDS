import unittest
import utils
from lab4.task9.src.hospital import Queue


class HospitalTest(unittest.TestCase):

    def test_should_add_mid(self):
        # given
        expected_result = [1, 3, 2, 5, 4]

        # when
        result = []
        queue = Queue()
        queue.add(1)
        queue.add(2)
        queue.add_mid(3)
        result.append(queue.remove())
        queue.add(4)
        queue.add_mid(5)
        result.append(queue.remove())
        result.append(queue.remove())
        result.append(queue.remove())
        result.append(queue.remove())


        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        queue = Queue()
        for i in range(10**5):
            queue.add_mid(i)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()