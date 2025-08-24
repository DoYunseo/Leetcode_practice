from typing import List
from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        maxi = 0
        hmap = defaultdict(int)
        for right in range(n):
            hmap[nums[right]] += 1

            # shrink the window to allow only at most one 0
            while nums[right] == 0 and hmap[nums[right]] > 1:
                hmap[nums[left]] -= 1
                left += 1
            maxi = max(maxi, right - left + 1)
            
        return maxi - 1
        

            

        