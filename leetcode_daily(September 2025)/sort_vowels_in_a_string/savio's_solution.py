class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        arr_of_vowels = []
        for char in s:
            if char in vowels:
                arr_of_vowels.append(char)
        arr_of_vowels.sort()
        print(arr_of_vowels)

        word_res = list(s)
        n = len(s)
        for i in range(n - 1, -1, -1):
            if word_res[i] in vowels:
                char = arr_of_vowels.pop()
                print(char)
                word_res[i] = char
            if len(arr_of_vowels) == 0:
                return "".join(word_res)
                


