class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        
        # groups[r] = smallest prefix sum
        groups = {r: float('inf') for r in range(k)}
        groups[0] = 0  # prefix sum before index 0
        
        ans = -10**18
        
        for i in range(1, n + 1):
            prefix += nums[i - 1]
            r = i % k
            
            ans = max(ans, prefix - groups[r])
            
            # store minimal prefix sum for this group
            groups[r] = min(groups[r], prefix)
        
        return ans