class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans =[]
        if num % 3 == 0:
            mid = num // 3
            for i in range(-1,2):
                ans.append(mid + i)
        else:
            pass
        return ans