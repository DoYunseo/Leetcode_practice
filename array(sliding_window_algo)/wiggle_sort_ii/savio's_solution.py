from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        std = sorted(nums)
        i = (n - 1) // 2
        j = n - 1
        for k in range(n):
            if k % 2 == 0:
                nums[k] = std[i]
                i-= 1
            else:
                nums[k] = std[j]
                j -= 1
             
        return nums
       