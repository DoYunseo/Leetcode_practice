from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(target)

        ans = 9999
        for ch in cnt_t.keys():
            if cnt_s[ch] // cnt_t[ch] < ans:
                ans = cnt_s[ch] // cnt_t[ch]
        
        return ans