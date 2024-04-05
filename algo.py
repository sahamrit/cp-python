from typing import *

def bin_search(arr: List, size: int) -> int:
    low = 0
    high = size - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] is True:
            high = mid
        else:
            low = mid + 1

    return high