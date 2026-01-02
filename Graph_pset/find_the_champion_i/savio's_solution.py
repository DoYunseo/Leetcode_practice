class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        champion = -1
        max_ones = float("-inf")
        for i, arr in enumerate(grid):
            counter = Counter(arr)
            if counter[1] > max_ones:
                champion = i
                max_ones = counter[1]
        return champion