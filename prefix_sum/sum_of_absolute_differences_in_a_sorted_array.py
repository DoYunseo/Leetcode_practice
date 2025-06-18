from typing import List
#solved it, and removed it
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_arr = [0] * n
        prefix_arr[0] = nums[0]
        for i in range(1, n):
            prefix_arr[i] = prefix_arr[i - 1] + nums[i]
        res = [0] * n
        for i in range(n):
            left_transformed = nums[i] * i
            left_sum = prefix_arr[i] - nums[i]
            left_total = left_transformed - left_sum
            right_transformed = nums[i] * (n - 1 - i)
            right_sum = prefix_arr[n - 1] - prefix_arr[i]
            right_total = right_sum - right_transformed
            res[i] = right_total + left_total
        return res
