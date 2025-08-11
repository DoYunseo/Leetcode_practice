from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        MOD = (10 ** 9) + 7
        power = 0
        result = []
        while n > 0:
            if n & 1:
                powers.append(2 ** power)
            power += 1
            n = n >> 1
        len_p = len(powers)
        for x, y in queries:
            p = 1
            for i in range(x, y + 1):
                p *= powers[i]
            result.append(p % MOD)
        return result


        


        