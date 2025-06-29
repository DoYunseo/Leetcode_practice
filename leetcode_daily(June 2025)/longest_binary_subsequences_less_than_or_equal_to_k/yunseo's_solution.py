class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cnt = 0
        value = 0
        bits = k.bit_length()
        
        for i, ch in enumerate(s[::-1]):
            if ch == '0':
                cnt += 1
            else:
                if i < bits and value + (1 << i) <= k:
                    value += 1 << i
                    cnt += 1
        
        return cnt 