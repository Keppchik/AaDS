import unittest
import lab6.utils as utils
from lab6.task2.src.phone_book import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = ["test2", "not found"]

        # when
        result = []
        phone_book = PhoneBook()
        phone_book.add("911", "police")
        phone_book.add("123", "test1")
        phone_book.add("456", "test2")
        result.append(phone_book.find("456"))
        phone_book.delete("911")
        result.append(phone_book.find("911"))

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        phone_book = PhoneBook()
        for i in range(10**5):
            phone_book.add(str(i), "name " + str(i))
            phone_book.find("name " + str(i))
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 6)
        self.assertLess(result[1], 512)


if __name__ == '__main__':
    unittest.main()