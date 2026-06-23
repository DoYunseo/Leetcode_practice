class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_b = Counter("balloon")
        count_t = Counter(text)
        max_c = float('inf')
        for key, val in count_b.items():
            if key in count_t:
                max_c = min(max_c, count_t[key] // val)
            elif key not in count_t:
                return 0
        return max_c