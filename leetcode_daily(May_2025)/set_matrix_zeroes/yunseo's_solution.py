class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        index = []

        # find index of all zeros
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    index.append([i,j])
        
        for i, j in index:
            for col in range(m):
                matrix[i][col] = 0
            for row in range(n):
                matrix[row][j] = 0