from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digiSet = Counter(digits)
        print(digiSet)
        res = set([])
        for i in range(100, 1000):
            if i % 2 == 0:
                s = str(i)
                convert = [int(char) for char in s]
                check_even_digits = Counter(convert)
                is_valid = True
                for key, val in check_even_digits.items():
                    if key not in digiSet:
                        is_valid = False
                        break

                    if val > digiSet[key]:
                        is_valid = False
                        break
                if is_valid:
                    res.add(i)
                
        return sorted(res)    