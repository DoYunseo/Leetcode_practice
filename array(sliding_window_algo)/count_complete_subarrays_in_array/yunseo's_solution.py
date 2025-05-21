class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        
        # 1. count the unique values in nums
        total_unique = len(set(nums))

        # 2. go through every subarray (i, j)
        for i in range(len(nums)):
            current_set = set()
            for j in range(i, len(nums)): 
                current_set.add(nums[j])
                if len(current_set) == total_unique:
                    cnt += 1  
                    
        return cnt