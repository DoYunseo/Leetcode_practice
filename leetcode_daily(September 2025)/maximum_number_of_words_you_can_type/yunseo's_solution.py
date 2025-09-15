class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0
        for word in words:
            if not set(word) & set(brokenLetters):
                count += 1
        return count
