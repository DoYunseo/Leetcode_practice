class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -float('inf'), -float('inf')]
        
        for num in nums:
            new_dp = dp[:]
            for r in range(3):
                new_mod = (r + num) % 3
                new_dp[new_mod] = max(new_dp[new_mod], dp[r] + num)
            dp = new_dp 
        return dp[0]