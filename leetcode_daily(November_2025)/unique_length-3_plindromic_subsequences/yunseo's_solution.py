class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # number of unique palindromes of length three
        n = len(s)
        ans = 0

        # Track first and last index of each character a-z 
        first = [-1] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        # for each character
        for c in range(26):
            if first[c] != -1 and first[c] < last[c]:
                left = first[c]
                right = last[c]

                # count unique characters in between
                middle = set(s[left+1:right])
                ans += len(middle)
        return ans