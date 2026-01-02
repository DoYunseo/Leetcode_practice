from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        hmap = defaultdict(int)
        res = []
        word = ""
        end = 0
        for i in range(n):
            if i - end + 1 == 10:
                hmap[s[end: i+1]] += 1
                end += 1
        for key, val in hmap.items():
            if val > 1:
                res.append(key)
        return res
