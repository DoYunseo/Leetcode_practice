class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(' ')
        ans = []

        for word in words:
            if len(word) <= 2:
                ans.append(word.lower())
            else:
                ans.append(word.capitalize())  
        
        ans = ' '.join(ans)
        return ans
            