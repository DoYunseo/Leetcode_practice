from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used_j = set([])
        counter = 0
        n = len(fruits)
        for i in range(n):
            for j in range(n):
                if j not in used_j and fruits[i] <= baskets[j]:
                    used_j.add(j)
                    break
                
        return len(baskets) - len(used_j)
