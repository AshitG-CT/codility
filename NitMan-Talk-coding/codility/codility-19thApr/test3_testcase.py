import unittest
from test3 import solution

class Testing(unittest.TestCase):
    def test_one(self):
        self.assertTrue(solution(A=[100, 100, 100, -10], D=["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))

    def test_two(self):
        self.assertTrue(solution(A=[180, -50, -25, -25], D=["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))

    def test_three(self):
        self.assertTrue(solution(A=[1, -1, 0, -105, 1], D=["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]))

    def test_four(self):
        self.assertTrue(solution(A=[100, 100, -10, -20, -30], D=["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]))

    def test_five(self):
        self.assertTrue(solution(A=[60, -60, -40, -20], D=["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]))

if __name__ == '__main__':
    unittest.main()