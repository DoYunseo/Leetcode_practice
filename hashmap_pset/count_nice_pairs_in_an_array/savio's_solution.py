from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        good_pairs = 0
        count = defaultdict(int)
        n = len(nums)

        def rev(x):
            s = str(x)
            return int(s[::-1])
        
        for i in range(n):
            diff = rev(nums[i]) - nums[i]
            if diff in count:
                good_pairs += count[diff]
            count[diff] += 1
            
        return good_pairs % (10 ** 9 + 7)