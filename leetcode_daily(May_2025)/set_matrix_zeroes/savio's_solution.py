from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rowum = [0] * m
        column = [0] * n
        for rows in range(m):
            for cols in range(n):
                if matrix[rows][cols] == 0:
                    column[cols] = 1
                    rowum[rows] = 1
        
        for rows in range(m):
            for cols in range(n):
                if column[cols] == 1 or rowum[rows] == 1:
                    matrix[rows][cols] = 0
        return matrix

        