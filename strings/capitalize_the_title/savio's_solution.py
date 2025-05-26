class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        n = len(words)
        for i in range(n):
            if len(words[i]) < 3:
                words[i] = words[i].lower()
            else:
                words[i] = words[i][0].upper() + words[i][1:].lower()
        return " ".join(words)
        