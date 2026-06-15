class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        map_a = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
        map_b = {i : chr(ord('z') - i) for i in range(26)}
        res = ""
        for word in words:
            rsum = 0
            for ch in word:
                rsum += weights[map_a[ch]]
            res += map_b[rsum % 26]
        return res