class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(num):
            return "0" in str(num)

        for i in range(1,n):  
            if has_zero(i) or has_zero(n-i):
                continue
            else:
                return [i,n-i]