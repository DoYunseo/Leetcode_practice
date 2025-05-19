from typing import List
from collections import Counter

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0] + nums[2] <= nums[1]:
            return "none"
        elif nums[1] + nums[2] <= nums[0]:
            return "none"
        else:
            count_sides = Counter(nums)
            if len(count_sides) == 1:
                return "equilateral"
            elif len(count_sides) == 2:
                return "isosceles"
            else:
                return "scalene"