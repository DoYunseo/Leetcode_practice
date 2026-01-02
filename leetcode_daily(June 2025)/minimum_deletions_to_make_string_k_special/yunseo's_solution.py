from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        freqs = sorted(counter.values())
        res = float('inf')

        for i in range(len(freqs)):
            deletions = 0
            target = freqs[i]

            for freq in freqs:
                if freq > target + k:
                    deletions += freq - (target + k)
                elif freq < target:
                    deletions += freq

            res = min(res, deletions)
        return res