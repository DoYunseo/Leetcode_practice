from collections import defaultdict
from typing import List
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        distinct_len = len(set(nums))

        start = 0
        end = 0
        n = len(nums) 
        count = 0
        for end  in range(n):
            hmap[nums[end]] += 1
            while len(hmap) >= distinct_len:
                count += n - end
                hmap[nums[start]] -= 1
                if hmap[nums[start]] == 0:
                    del hmap[nums[start]]
                start += 1
        return count

        