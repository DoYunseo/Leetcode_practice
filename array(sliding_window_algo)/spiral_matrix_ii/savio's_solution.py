from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]* n for _ in range(n)]
        top, left, right, bottom = 0, 0, n - 1, n - 1
        count = 1
        while count <= n * n and left <= right and top <= bottom:
            for i in range(left, right + 1):
                ans[top][i] = count
                count += 1
            top += 1
            for i in range(top, bottom + 1):
                ans[i][right] = count 
                count += 1
            right -= 1
            for i in range(right, left - 1, - 1):
                ans[bottom][i] = count
                count += 1
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                ans[i][left] = count
                count += 1
            left += 1
        return ans