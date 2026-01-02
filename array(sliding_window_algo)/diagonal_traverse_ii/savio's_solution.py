from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        hmap = defaultdict(list)
        n = len(nums)

        for row in range(n):
            for col in range(len(nums[row])):
                hmap[row + col].append(nums[row][col])

        # reverse hmap

        res = []
        for key in sorted(hmap.keys()):
            # Reverse to get correct traversal order
            res.extend(hmap[key][::-1])
        return res
