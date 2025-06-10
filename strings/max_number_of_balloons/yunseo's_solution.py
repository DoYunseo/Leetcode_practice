from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        required = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n':1
        }
        count = defaultdict(int)
        
        for ch in text:
            if ch in required:
                count[ch] += 1
        
        min_times = float('inf')
        for ch in required:
            min_times = min(min_times, count[ch] // required[ch])
        
        return min_times
        
        