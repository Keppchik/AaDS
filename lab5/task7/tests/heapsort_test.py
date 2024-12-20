import unittest
from random import randint
from lab5.task7.src.heapsort import heapsort


class HeapsortTest(unittest.TestCase):

    def test_should_heapsort_avg(self):
        # given
        array = [randint(-10**9, 10**9) for _ in range(10**5)]
        expected_result = sorted(array)

        # when
        heapsort(array)

        # then
        self.assertEqual(expected_result, array)

    def test_should_heapsort_worst(self):
        # given
        array = [i for i in range(10**5, -1, -1)]
        expected_result = sorted(array)

        # when
        heapsort(array)

        # then
        self.assertEqual(expected_result, array)

    def test_should_heapsort_best(self):
        # given
        array = [i for i in range(10**5)]
        expected_result = array

        # when
        heapsort(array)

        # then
        self.assertEqual(expected_result, array)


if __name__ == '__main__':
    unittest.main()

