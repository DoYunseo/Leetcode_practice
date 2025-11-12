import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # gcd: greatest common divisor
        n = len(nums)
        flag = False

        # Case 1: 1 is already in the list
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        # Case 2: invalid
        g = 0
        for x in nums:
            g = gcd(g,x)
        if g != 1:
            return -1
        
        # Case 3: find the minimun length of subset where gcd is 1
        best = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break
        return n + best - 2