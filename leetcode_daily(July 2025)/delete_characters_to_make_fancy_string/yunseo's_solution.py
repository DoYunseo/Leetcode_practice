class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        
        for i in range(len(s)):
            if i >= 2 and s[i] == s[i-1] == s[i-2]:
                continue
            ans += s[i]
        return ans