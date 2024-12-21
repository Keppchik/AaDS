import unittest
from random import randint
import utils
from lab7.task1.src.coin_exchange import min_coins


class CoinExchangeTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = 9

        # when
        result = min_coins(34, [1, 3, 4])

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        money = 10**3
        coins_list = [randint(1,10**3) for _ in range(100)]
        coins_set = set(coins_list)
        time_start = utils.start_tracking()

        # when
        min_coins(money, coins_set)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 1)


if __name__ == '__main__':
    unittest.main()