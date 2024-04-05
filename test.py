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

    def test_bfs(self):
        
        # case 1
        adj = [[] for _ in range (10)]
        adj[0] = [1, 2, 3, 4]
        adj[1] = [5, 6]
        adj[2] = [7, 8]
        adj[3] = [9]
        adj[4] = []

        self.assertEqual(list(range(10)), bfs(adj, 0))

        # case 1
        adj = [[] for _ in range (10)]
        adj[0] = [1, 2, 3, 4]
        adj[1] = [5, 6]
        adj[2] = [7, 8]
        adj[3] = [9]
        adj[4] = []

        self.assertEqual(list(range(10)), bfs(adj, 0))

        adj = [[] for _ in range (10)]
        adj[1] = [4, 5, 6]
        adj[4]  = [3]
        adj[5] = [2, 7]
        
        self.assertEqual([1, 4, 5, 6, 3, 2, 7], bfs(adj, 1))

        adj = [[] for _ in range (10)]
        adj[5] = [2, 3, 4]
        adj[2]  = [8]
        adj[3] = [6]
        adj[4] = [1]
        
        self.assertEqual([5, 2, 3, 4, 8, 6, 1], bfs(adj, 5))

if __name__ == "__main__":
    unittest.main()