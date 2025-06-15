class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        total_weight = n * n * w
        while total_weight > maxWeight:
            total_weight -= w
        return total_weight // w

        