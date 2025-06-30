from typing import List
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        word = ""
        for i in range(n):
            word += s[i]
            if len(word) == k:
                res.append(word)
                word = ""
        while len(word) > 0:
            if len(word) == k:
                res.append(word)
                break
            word += fill
        return res