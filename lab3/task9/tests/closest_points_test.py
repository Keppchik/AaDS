import unittest
from lab3.task9.src.closest_points import closest_points

class ClosestPointsTest(unittest.TestCase):

    def test_should_closest_points1(self):
        expected_result = "5.0"
        data = [(0,0),(3,4)]
        result = f"{closest_points(data, 0, 2):.6}"
        self.assertEqual(result, expected_result)

    def test_should_closest_points2(self):
        expected_result = "0.0"
        data = [(7,7),(1,100),(4,8),(7,7)]
        result = f"{closest_points(data, 0, 4):.6}"
        self.assertEqual(result, expected_result)

    def test_should_closest_points3(self):
        expected_result = "1.41421"
        data = [(4,4),(-2,-2),(-3,-4),(-1,3),(2,3),(-4,0),(1,1),(-1,-1),(3,-1),(-4,2),(-2,4)]
        data.sort()
        result = f"{closest_points(data, 0, 11):.6}"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()