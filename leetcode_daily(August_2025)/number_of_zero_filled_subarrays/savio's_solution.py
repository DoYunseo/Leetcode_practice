from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        counter = 0
        streak_count = 0
        for right in range(n):
            if nums[right] == 0:
                streak_count += 1
            else:
                counter += streak_count * (streak_count + 1) // 2
                streak_count = 0
        counter += streak_count * (streak_count + 1) // 2
        return counter
            
        