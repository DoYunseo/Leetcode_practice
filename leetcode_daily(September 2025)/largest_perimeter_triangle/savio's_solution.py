from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        perimeter = 0
        for i in range(n - 1, 1, -1):
            print(nums[i])
            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i - 1] + nums[i - 2] + nums[i]
        return perimeter
