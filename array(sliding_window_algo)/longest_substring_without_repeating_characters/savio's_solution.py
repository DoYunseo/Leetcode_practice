from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mini = 0
        left = 0
        n = len(s)
        d = defaultdict(int)
        for right in range(n):
            while s[right] in d:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
            mini = max(mini, right - left + 1)
            d[s[right]] += 1
        return mini