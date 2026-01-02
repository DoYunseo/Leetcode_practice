class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left = 0
        result = 0

        for right in range(len(nums)):
            if right - left + 1 == 3:
                if (nums[right] + nums[left]) * 2 == nums[left + 1]:
                    result += 1
                left += 1
        return result