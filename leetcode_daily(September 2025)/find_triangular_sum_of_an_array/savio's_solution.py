from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        temp = []
        n = len(nums)

        while n > 1:
            for i in range(n - 1):
                r_sum = (nums[i] + nums[i + 1]) % 10
                temp.append(r_sum)
            nums = temp
            temp = []
            n -= 1
        return nums[-1]
