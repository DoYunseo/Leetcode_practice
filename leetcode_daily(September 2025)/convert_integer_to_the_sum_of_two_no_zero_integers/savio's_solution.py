from typing import List
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def does_not_contain_zero(i):
            s = str(i)
            m_set = set(s)
            if "0" in m_set:
                return False
            return True
        
        for a in range(1, n):
            b = n - a
            if does_not_contain_zero(a) and does_not_contain_zero(b):
                return [a, b]