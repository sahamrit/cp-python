from typing import *

def bin_search(arr: List[int], size: int) -> int:
    low = 0
    high = size - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] is True:
            high = mid
        else:
            low = mid + 1

    return high

def bfs(adj: List[List[int]], root: int) -> List[int]:
    queue: List[int] = [root]
    answer = []
    visit = [False for _ in range(10000)]
    visit[root] = True
    while len(queue):
        node = queue.pop()
        answer.insert(0, node)
        for nbr in adj[node]:
            if not visit[nbr]:
                queue.insert(0, nbr)
                visit[nbr] = True

    answer.reverse()
    return answer

class DSU:
    def __init__(self) -> None:
        self.parent: List[List[int]] = [i for i in range(10)]
        self.size: List[int] = [1 for i in range(10)]

    def find(self, idx: int) -> int:
        if idx != self.parent[idx]:
            # binary lifting
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

    def merge(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.size[root_a] >= self.size[root_b]:
                self.parent[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parent[root_a] = root_b
                self.size[root_b] += self.size[root_a]

    def same_set(self, a: int, b: int):
        return self.find(a) == self.find(b)


class BinTree:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert(self, num) -> None:
        curr = self
        while curr is not None:
            if num < curr.val:
                if curr.left is None:
                    curr.left = BinTree(num)
                    break
                curr = curr.left
            elif num > curr.val:
                if curr.right is None:
                    curr.right = BinTree(num)
                    break
                curr = curr.right
            else: break

    def inorder(self) -> List[int]:
        curr = self
        ans = []
        stack = []
        while curr or len(stack):
            if curr is None:
                x = stack.pop(0)
                ans.insert(0, x.val)
                curr = x.right
            else:
                stack.insert(0, curr)
                if curr.left is not None:
                    curr = curr.left
                    continue
                if curr.left is None:
                    ans.insert(0, curr.val)
                    stack.pop(0)
                    curr = curr.right
        ans.reverse()
        return ans

    def postorder(self) -> List[int]:
        curr = self
        ans = []
        stack = []
        while curr or len(stack):
            if curr is None:
                x = stack.pop(0)
                if x[1] == 0:
                    stack.insert(0, (x[0], 1))
                    curr = x[0].right
                else:
                    ans.insert(0, x[0].val)
            else:
                stack.insert(0, (curr, 0))
                if curr.left is not None:
                    curr = curr.left
                    continue
                if curr.left is None:
                    x = stack.pop(0)
                    stack.insert(0, (x[0], 1))
                    curr = curr.right
        ans.reverse()
        return ans

class SegmentTree:
    def __init__(self, arr) -> None:
        self.size = len(arr)
        self.t = [0 for _ in range(4 * self.size)]
        self.arr = arr


    def build_tree(self, idx, low, high):
        if low == high:
            self.t[idx] = self.arr[low]
            return
        mid = (low + high) // 2

        self.build_tree(2* idx, low, mid)
        self.build_tree(2 *idx + 1, mid + 1, high)

        self.t[idx] = self.t[2 * idx] + self.t[2 * idx + 1]

    def build(self):
        self.build_tree(1, 0, self.size - 1)

    def query(self, idx, l, r, tl, tr):
        if l > r:
            return 0
        
        if (l == tl) and (r == tr):
            return self.t[idx]

        mid = (tl + tr) // 2

        return self.query(2 * idx, l, min(r, mid), tl, mid) + self.query(2 * idx + 1, max(l, mid + 1), r, mid + 1, tr)

