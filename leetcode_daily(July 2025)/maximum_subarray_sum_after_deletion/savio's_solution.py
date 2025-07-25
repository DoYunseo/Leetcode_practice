class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxi = max(nums)
        visited = set()
        total = 0
        if maxi < 0:
            return maxi
        else:
            for num in nums:
                if num not in visited and num > 0:
                    visited.add(num)
                    total += num
        return total



        