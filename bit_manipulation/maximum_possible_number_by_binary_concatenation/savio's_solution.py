from itertools import permutations
from typing import List

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        # steps to solving this problem

        """
        get the permutations of the nums array
        concatenate the binary representation of them
        then return the maximum
        """
        result = 0
        for p in permutations(nums):
            new_lst = list(p)
            temp_res = 0
            for num in new_lst:
                temp_res  = temp_res << num.bit_length()
                temp_res = temp_res | num
            result = max(result, temp_res)
        return result
            
        