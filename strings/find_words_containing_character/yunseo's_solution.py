class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = set()
        for i in range(len(words)):
            if x in words[i]:
                ans.add(i)
        return list(ans)