from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        vowels = set("aeiou")

        max1, max2 = 0, 0
        for k, v in count.items():
            if k in vowels:
                max1 = max(max1, v)
            else:
                max2 = max(max2, v)
        return max1 + max2
