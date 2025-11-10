class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2**31) and divisor == -1:
            return (2**31) - 1
        nw = str(dividend / divisor)
        nw = nw.split(".")

        return int(nw[0])
