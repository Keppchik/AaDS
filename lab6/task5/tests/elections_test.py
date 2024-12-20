import unittest
import lab6.utils as utils
from lab6.task5.src.elections import Election


class ElectionsTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = ["ivanov 900", "petr 70", "tourist 3"]

        # when
        result = []
        election = Election()
        election.add("ivanov", "100")
        election.add("ivanov", "500")
        election.add("ivanov", "300")
        election.add("petr", "70")
        election.add("tourist", "1")
        election.add("tourist", "2")
        result = election.votes()

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        election = Election()
        for i in range(10**5):
            election.add("name " + str(i), str(i))
        election.votes()
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 64)


if __name__ == '__main__':
    unittest.main()