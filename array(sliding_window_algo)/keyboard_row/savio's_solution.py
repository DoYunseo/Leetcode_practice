class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = set("qwertyuiop")
        row_2 = set("asdfghjkl")
        row_3 = set("zxcvbnm")
        print(row_2)

        word_set = defaultdict(dict)
        for idx, word in enumerate(words):
            word_set[idx] = set(word.lower())
        print(word_set)
        return [words[word] for word, val in word_set.items() if val - row_1 == set() or val - row_2 == set() or val - row_3 == set()]