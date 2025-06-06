from typing import List
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        
        # Count odd-valued rows and columns
        odd_rows = sum(1 for x in rows if x % 2 == 1)
        odd_cols = sum(1 for y in cols if y % 2 == 1)
        
        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols 


