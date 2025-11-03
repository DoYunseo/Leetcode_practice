class Solution:
    def smallestNumber(self, n: int) -> int:
        k = n.bit_length()
        while True:
            candidate = (1 << k) - 1 
            if candidate >= n:
                return candidate
            k += 1