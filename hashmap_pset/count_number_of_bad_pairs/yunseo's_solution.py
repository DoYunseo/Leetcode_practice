class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # i < j 
        # j - i != nums[j] - nums[i]
        # Good pair: nums[i] - i == nums[j] - j
        # count all the good pairs
        n = len(nums)
        good = 0
        diff_count = {}
        
        for i in range(n):
            key = nums[i] - i
            print(key)

            if key in diff_count:
                good += diff_count[key]
                diff_count[key] += 1 
            else:
                diff_count[key] = 1
        
        total_pairs = n * (n-1) // 2
        print("good:", good)
        print("total_pairs:", total_pairs)
        return total_pairs - good