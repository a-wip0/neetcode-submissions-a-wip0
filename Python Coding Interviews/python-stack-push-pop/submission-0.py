from typing import List
from collections import deque


def reverse_list(arr: List[int]) -> List[int]:
    new_list = deque()
    for a in arr:
        new_list.appendleft(a)

    return list(new_list)


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
