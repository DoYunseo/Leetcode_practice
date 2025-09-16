class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        sentence = text.split(" ")
        mset = set(brokenLetters)
        count = 0
        for word in sentence:
            if any(char in mset for char in word):
                continue
            else:
                count += 1
        return count
