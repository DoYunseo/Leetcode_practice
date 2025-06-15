# just added some comments!
from typing import List
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = []
        for num in nums:
            if count[num] >= len(res):
                res.append([])
            res[count[num]].append(num)
            count[num] += 1
        return res
