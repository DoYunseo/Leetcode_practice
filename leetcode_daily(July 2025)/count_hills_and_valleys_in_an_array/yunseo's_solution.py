class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1 

        cnt = 0
        for i in range(1,len(nums)-1):
            tmp = nums[i-1:i+2]
            if tmp[1] == max(tmp):
                cnt += 1
            elif tmp[1] == min(tmp):
                cnt += 1
        
        return cnt