class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) <= k:
            for c in word:
                if c == "z":
                    word += a
                else:
                    word += chr(ord(c) + 1)
        return word[k - 1]
        