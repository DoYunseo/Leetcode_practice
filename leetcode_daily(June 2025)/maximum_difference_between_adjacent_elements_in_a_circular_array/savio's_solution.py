from typing import List
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = -1000
        for i in range(n):
           maxi = max(maxi, abs(nums[(i + 1) % n] - nums[i % n]))
        return maxi
