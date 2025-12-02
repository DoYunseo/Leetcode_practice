from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ycount = defaultdict(int)
        
        # 1. count the number of points for each y
        for x, y in points:
            ycount[y] += 1
        
        # 2. the number of 2-point combinations in that y-layer
        comb = []
        for y, cnt in ycount.items():
            if cnt >= 2:
                c = cnt * (cnt - 1) // 2
                comb.append(c)
        
        # impossible case
        if len(comb) < 2:
            return 0
        
        # 3. sum of every C_i * C_j 
        S = sum(comb) % MOD
        S2 = sum((c * c) % MOD for c in comb) % MOD
        
        ans = (S * S - S2) % MOD
        ans = (ans * pow(2, MOD - 2, MOD)) % MOD  # /2 mod
        
        return ans