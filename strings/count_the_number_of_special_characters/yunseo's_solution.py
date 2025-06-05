class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()

        for letter in word:
            if letter.islower() == True:
                lower_set.add(letter)
            elif letter.isupper() == True:
                upper_set.add(letter.lower())
        
        return len(lower_set & upper_set)