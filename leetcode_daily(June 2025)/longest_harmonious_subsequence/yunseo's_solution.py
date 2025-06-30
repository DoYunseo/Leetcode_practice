from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0 

        for num in count:
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])

        return res