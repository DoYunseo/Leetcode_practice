class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        n = len(cost)
        total = 0
        for i in range(n):
            if (i + 1) % 3 != 0:
                total += cost[i]

        return total