import unittest
from lab4.task13.src.task13 import Queue, Stack


class Task13Test(unittest.TestCase):

    def test_should_stack(self):
        # given
        expected_result = "6 4 3 2 1"


        # when
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.pop()
        stack.push(6)
        result = repr(stack)

        # then
        self.assertEqual(result, expected_result)

    def test_should_queue(self):
        # given
        expected_result = "2 3 4 5 6"

        # when
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        queue.dequeue()
        queue.enqueue(6)
        result = repr(queue)

        # then
        self.assertEqual(result, expected_result)

    def test_should_queue_max_size(self):
        # given
        expected_result = "1 2 3"

        # when
        queue = Queue(max_size=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        result = repr(queue)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()