import numpy as np

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        arr = np.array(nums)
        uniques = np.unique(arr)
        for unique in uniques:
            if nums.count(int(unique)) == n:
                return int(unique)
