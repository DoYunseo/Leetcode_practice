class Solution:
    def minOperations(self, s: str) -> int:
        cnt1 = 0  #"101010"
        cnt2 = 0  #"010101"

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != "0":
                    cnt1 += 1
                if s[i] != "1":
                    cnt2 += 1
            else:
                if s[i] != "1":
                    cnt1 += 1
                if s[i] != "0":
                    cnt2 += 1
        return min(cnt1, cnt2)