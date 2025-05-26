from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small = Counter([char for char in word if char.islower()])
        big = Counter([char for char in word if char.isupper()])
        count = 0
        for key in small.keys():
            if key.upper() in big:
                count += 1
        return count

        