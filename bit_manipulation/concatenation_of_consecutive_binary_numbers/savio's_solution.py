class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 1

        for i in range(2, n + 1):
            result = result << i.bit_length()
            result = result | i
            result = result % (10 ** 9 + 7)
        return result 
        

