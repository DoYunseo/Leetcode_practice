from typing import List
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s_digits, d_digits = 0, 0
        for num in nums:
            s = str(num)
            if len(s) == 1:
                s_digits += int(s)
            else:
                d_digits += int(s)
        return True if s_digits > d_digits or s_digits < d_digits else False