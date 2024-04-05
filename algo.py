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
