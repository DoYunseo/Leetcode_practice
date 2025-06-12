from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        max_even_freq, max_odd_freq = float("-inf"), float("-inf")
        min_odd_freq, min_even_freq = float("inf"), float("inf")

        for val in count.values():
            if val % 2 == 0 and val > max_even_freq:
                max_even_freq = val
            if val % 2 != 0 and val > max_odd_freq:
                max_odd_freq = val
            if val % 2 == 0 and val < min_even_freq:
                min_even_freq = val
            if val % 2 != 0 and val < min_odd_freq:
                min_odd_freq = val
        print(min_even_freq, min_odd_freq, max_even_freq, max_odd_freq)

        maxi = float("-inf")
        if abs(max_odd_freq - min_even_freq) > maxi: 
            maxi = max(maxi, max_odd_freq - min_even_freq)
        else:
            maxi = max(maxi, min_odd_freq - max_even_freq)
        return maxi
