class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        n = len(matrix)
        m = len(matrix[0])
        colset = set()
        rowset = set()

        # add col,row which has zero inside
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    colset.add(i)
                    rowset.add(j)
        
        for i in colset:
            matrix[i] = [0]*m

        for i in range(n):
            for j in rowset:
                matrix[i][j] = 0