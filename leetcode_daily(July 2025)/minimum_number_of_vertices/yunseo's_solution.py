class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        exist = set()
        for i in range(len(edges)):
            exist.add(edges[i][1])
        
        ans = []
        for i in range(n):
            if i not in exist:
                ans.append(i)
        return ans