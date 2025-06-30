class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(0,n,k):
            group = s[i:i+k]
            if len(group) < k:
                group += fill * (k-len(group)) 
            ans.append(group)
            print(ans)
        return ans