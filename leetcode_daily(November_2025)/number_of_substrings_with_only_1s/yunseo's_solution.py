class Solution:
    def numSub(self, s: str) -> int:
        length = len(s)
        total, con = 0, 0

        for i in range(length):
            if s[i] == '0':
                total += con * (con + 1) // 2
                con = 0 
            else:
                con += 1
        total += con * (con + 1) // 2
        total %= 10**9 + 7
        return total