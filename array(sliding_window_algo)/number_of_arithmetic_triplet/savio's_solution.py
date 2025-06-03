from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)
        seen = set([])
        for cpos in range(n - 2):
            left, right = cpos + 1, n - 1
            while left < right:
                if nums[left] - nums[cpos] == diff:
                    while left < right and nums[right] - nums[left] != diff:
                        right -= 1
                    if (cpos, left, right) not in seen:
                        seen.add((cpos, left, right))
                left += 1
        for item in seen:
            if len(item) == len(set(item)):
                count += 1
        return count