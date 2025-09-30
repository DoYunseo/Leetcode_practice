class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        initial_n = len(nums)
        for _ in range(initial_n - 1):
            n = len(nums)
            if n == 1:
                return nums[0]
            else:
                newNums = [0 for i in range(n-1)]
                for i in range(n-1):
                    newNums[i] = (nums[i] + nums[i+1]) % 10
                nums = newNums
        ans = nums[0]
        return ans