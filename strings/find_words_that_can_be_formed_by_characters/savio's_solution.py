from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars = Counter(chars)
        good_len = 0
        for word in words:
            count_word = Counter(word)
            flag = False
            for key, val in count_word.items():
                if key not in count_chars:
                    flag = True
                    break
                elif val > count_chars[key]:
                    flag = True
                    break
            if not flag:
                good_len += len(word)
        return good_len


                    
        