class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        cnt = 0
        
        while s % k != 0:
            s -= 1
            cnt += 1
        return cnt