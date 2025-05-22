from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        char_count = Counter(chars)
        for word in words:
            word_count = Counter(word)
            flag = True
            for i in range(97,123):
                if char_count[chr(i)] < word_count[chr(i)]:
                    flag = False
            if flag == True:
                sum += len(word)
        return sum