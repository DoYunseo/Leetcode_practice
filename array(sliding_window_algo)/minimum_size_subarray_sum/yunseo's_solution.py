class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(n):
            total += nums[right]

            # update till it gets over the target number
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0
        else:
            return min_len