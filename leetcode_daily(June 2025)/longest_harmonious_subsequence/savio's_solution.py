from typing import List
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ## Approach to solving this problem:

        '''
        1. We need to count each element in the array
        2. For the key, if there exist key + 1 in the counter, then there is a harmonious subsequence
        3. All that is needed is to add the frequency of the key, and that of key + 1
        4. Update max counter
        '''
        maps = Counter(nums)
        max_res = 0
        for key in maps.keys():
            if key + 1 in maps:
                max_res = max(max_res, maps[key]+ maps[key + 1])
        return max_res
        