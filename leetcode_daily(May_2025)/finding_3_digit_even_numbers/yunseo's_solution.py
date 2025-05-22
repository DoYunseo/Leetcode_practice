class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue
                    a, b, c = digits[i], digits[j], digits[k]
                    if a == 0:
                        continue  # leading zero
                    if c % 2 != 0:
                        continue  # not even
                    num = a * 100 + b * 10 + c
                    ans.add(num)
        return sorted(ans)