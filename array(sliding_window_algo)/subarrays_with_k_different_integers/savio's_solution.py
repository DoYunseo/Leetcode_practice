from collections import defaultdict
from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarray_with_at_most(nums, k):
            hmap = defaultdict(int)
            start = 0
            n = len(nums) 
            count = 0
            for end  in range(n):
                hmap[nums[end]] += 1
                while len(hmap) > k:
                    hmap[nums[start]] -= 1
                    if hmap[nums[start]] == 0:
                        del hmap[nums[start]]
                    start += 1
                count += end - start + 1
            return count
        #the trick is to use knowledge from combinatorics. ciunt Exactly k = (count At most k) - (count At most k - 1)
        result = subarray_with_at_most(nums, k) - subarray_with_at_most(nums, k - 1)
        return result
        