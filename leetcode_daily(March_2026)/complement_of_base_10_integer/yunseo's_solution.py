class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = list(format(n, 'b'))
        for i in range(len(s)):
            if s[i] == "1":
                s[i] = "0"
            else:
                s[i] = "1"
        s = ''.join(s)
        return int(s,2)