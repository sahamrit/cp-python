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

    def test_dsu(self):
        dsu = DSU()

        dsu.merge(0, 1)

        self.assertEqual(True, dsu.same_set(0, 1))
        self.assertEqual(False, dsu.same_set(0, 9))
        self.assertEqual(False, dsu.same_set(4, 5))

        dsu.merge(0, 5)
        self.assertEqual(True, dsu.same_set(5, 1))
        self.assertEqual(True, dsu.same_set(5, 0))
        self.assertEqual(False, dsu.same_set(4, 5))

        dsu.merge(4, 5)
        self.assertEqual(True, dsu.same_set(4, 5))
        self.assertEqual(True, dsu.same_set(1, 5))
        self.assertEqual(True, dsu.same_set(1, 4))
        self.assertEqual(False, dsu.same_set(1, 2))

        # [0 1 4 5]

        self.assertEqual(0, dsu.find(0))
        self.assertEqual(0, dsu.find(1))
        self.assertEqual(0, dsu.find(4))
        self.assertEqual(0, dsu.find(5))

        dsu.merge(2, 7)
        dsu.merge(2, 8)
        dsu.merge(8, 9)

        self.assertEqual(2, dsu.find(7))
        self.assertEqual(2, dsu.find(8))
        self.assertEqual(2, dsu.find(9))

        dsu.merge(4, 2)
        self.assertEqual(0, dsu.find(7))
        self.assertEqual(0, dsu.find(8))
        self.assertEqual(0, dsu.find(9))
        self.assertEqual(0, dsu.find(0))
        self.assertEqual(0, dsu.find(1))
        self.assertEqual(0, dsu.find(4))
        self.assertEqual(0, dsu.find(5))

    def test_bin_tree(self):
        tree = BinTree(5)
        tree.insert(10)
        tree.insert(100)
        tree.insert(0)
        tree.insert(-10)
        tree.insert(90)

        self.assertEqual([-10, 0, 5, 10, 90, 100], tree.inorder())
        self.assertEqual([-10, 0, 90, 100, 10, 5], tree.postorder())

        tree = BinTree(45)
        tree.insert(19)
        tree.insert(10)
        tree.insert(65)
        tree.insert(-170)
        tree.insert(-200)

        self.assertEqual([-200, -170, 10, 19, 45, 65], tree.inorder())
        self.assertEqual([-200, -170, 10, 19, 65, 45], tree.postorder())


if __name__ == "__main__":
    unittest.main()