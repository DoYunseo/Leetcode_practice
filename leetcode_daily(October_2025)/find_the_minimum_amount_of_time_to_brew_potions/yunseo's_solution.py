from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        if m == 0 or n == 0:
            return 0

        # finish_prev[i] = time when ith wizard finished potion j-1
        finish_prev = [0] * n

        # potion 0
        cum = 0  # prefix sum
        for i in range(n):
            prefix_i = cum
            p = skill[i] * mana[0]
            start_i = 0 + prefix_i
            finish_prev[i] = start_i + p
            cum += p

        # potion 1 to m-1 
        for j in range(1, m):
            prefix = [0] * n
            p_col = [0] * n
            cum = 0
            for i in range(n):
                prefix[i] = cum
                p = skill[i] * mana[j]
                p_col[i] = p
                cum += p

            Sj = max(finish_prev[i] - prefix[i] for i in range(n))

            finish_curr = [0] * n
            for i in range(n):
                start_i = Sj + prefix[i]
                finish_curr[i] = start_i + p_col[i]

            finish_prev = finish_curr

        return finish_prev[-1]