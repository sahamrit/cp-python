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

