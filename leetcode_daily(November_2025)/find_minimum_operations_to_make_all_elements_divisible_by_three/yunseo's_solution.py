class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums) 
        cnt = 0
        for i in range(n):
            if nums[i] % 3 != 0:
                cnt += 1
        return cnt