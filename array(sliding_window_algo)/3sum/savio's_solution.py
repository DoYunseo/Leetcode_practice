from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, ans = len(nums), []
        for cpos in range(n - 2):
            if nums[cpos] > 0:
                break
            if cpos == 0 or nums[cpos] != nums[cpos - 1]:
                left, right = cpos + 1, n - 1
                while left < right:
                    csum = nums[cpos] + nums[left] + nums[right]
                    if csum > 0:
                        right -= 1
                    elif csum < 0:
                        left += 1
                    else:
                        ans.append([nums[cpos], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return ans 