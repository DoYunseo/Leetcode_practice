class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = nums[0]
        
        # subsequence number should be 1 or more
        cnt = 1

        for num in nums:
            if num - start > k:
                cnt += 1
                start = num
       
        return cnt