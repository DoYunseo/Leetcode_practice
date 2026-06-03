class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # check at most 4 times
        n = len(mat)

        if mat == target:
            return True
        
        for _ in range(3):
            new = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    new[j][n-1-i] = mat[i][j]
            if new == target:
                return True
            mat = new 
        
        return False