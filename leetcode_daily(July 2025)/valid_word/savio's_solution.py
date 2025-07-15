class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        h_set = {"a", "e", "i", "o", "u"}
        hmap = defaultdict(int)

        for c in word:
            if c.lower() in h_set and c.isupper():
                hmap["vowel"] += 1
                hmap["upper"] += 1
            elif c.lower() in h_set:
                hmap["vowel"] += 1
            elif c.isupper() and c.isalpha():
                hmap["upper"] += 1
                hmap["consonants"] +=1
            elif c.isnumeric():
                hmap["number"] += 1
            elif c.isalpha():
                hmap["consonants"] += 1
            else:
                hmap["symbol"] += 1
        if ("symbol" in hmap) or ("consonants" not in hmap) or ("vowel" not in hmap):
            return False
        else:
            return True
            
        
