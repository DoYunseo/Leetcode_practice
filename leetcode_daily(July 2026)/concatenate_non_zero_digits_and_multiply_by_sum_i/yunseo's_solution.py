class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)
        x = ''
        for c in n:
            if c != '0':
                x += c
        
        if len(x) == 0:
            x = '0'

        sum_n = 0
        for c in x:
            sum_n += int(c)

        return int(x) * sum_n 