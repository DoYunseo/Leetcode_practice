class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        digit_no_zero = ""
        sumd = 0
        for c in s:
            if c == "0":
                continue
            digit_no_zero += c
            sumd += int(c)
        return sumd * int(digit_no_zero) if len(digit_no_zero) > 0 else 0

        
        