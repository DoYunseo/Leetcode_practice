from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c_word1 = Counter(word1)
        c_word2 = Counter(word2)
        res = []
        for key, val in c_word1.items():
            if key not in c_word2:
                res.append(val)
            else:
                res.append(abs(val - c_word2[key]))
        for key, val in c_word2.items():
            if key not in c_word1:
                res.append(val)
        return True if max(res) <= 3 else False
        