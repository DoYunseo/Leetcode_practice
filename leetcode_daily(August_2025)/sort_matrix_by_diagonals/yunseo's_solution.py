class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diags = defaultdict(list)

        for i in range(n):
            for j in range(n):
                key = i - j          
                diags[key].append(grid[i][j])  

        # i - j >= 0 : decreasing
        # i - j < 0  : increasing
        for key in diags:
            if key >= 0:
                diags[key].sort(reverse=True)  
            else:
                diags[key].sort()           

        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = diags[key].pop(0) 

        return grid