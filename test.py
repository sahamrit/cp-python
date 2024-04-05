import unittest
import random
from algo import *

class Algorithms(unittest.TestCase):

    def test_bin_search(self):
        N = 100
        tests = 1000
        for _ in range(tests):
            arr = [False for _ in range(N)]
            idx = random.randint(0, N - 1)
            for i in range(idx, N):
                arr[i] = True
            self.assertEqual(idx, bin_search(arr, N))


if __name__ == "__main__":
    unittest.main()