import unittest
import lab6.utils as utils
from lab6.task4.src.asociated_array import AsociatedArray


class AsociatedArrayTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = ["a", "a", "c", "<none>", "<none>"]

        # when
        result = []
        asociated_array = AsociatedArray()
        asociated_array.put("one", "a")
        asociated_array.put("two", "b")
        asociated_array.put("three", "c")
        result.append(asociated_array.get("one"))
        result.append(asociated_array.prev("two"))
        result.append(asociated_array.next("two"))
        asociated_array.delete("three")
        result.append(asociated_array.get("three"))
        result.append(asociated_array.get("four"))

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        asociated_array = AsociatedArray()
        for i in range(5 * 10**5):
            asociated_array.put("testkey" + str(i), "testvalue" + str(i))
            asociated_array.get("testkey" + str(i))
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 4)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()