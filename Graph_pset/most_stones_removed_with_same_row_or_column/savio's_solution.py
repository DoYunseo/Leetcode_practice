from typing import List
from collections import defaultdict

class DisjointSet():
    def __init__(self, n, stones):
        self.parent = {tuple(stones[i]): tuple(stones[i]) for i in range(n)}
        self.rank = {tuple(stones[i]): 0 for i in range(n)}
    
    def ulp_parent(self, node):
        if node == self.parent[node]:
            return node
        else:
            self.parent[node] = self.ulp_parent(self.parent[node])
            return self.parent[node]
    def unite(self, n1, n2):
        ulp1, ulp2 = self.ulp_parent(n1), self.ulp_parent(n2)
        if self.rank[ulp1] == self.rank[ulp2]:
            self.parent[ulp1] = ulp2
            self.rank[ulp2] += 1
        elif self.rank[ulp1] > self.rank[ulp2]:
            self.parent[ulp2] = ulp1
        else:
            self.parent[ulp1] = ulp2
    def same_parent(self, n1, n2):
        ulp1, ulp2 = self.ulp_parent(n1), self.ulp_parent(n2)
        if ulp1 == ulp2:
            return True
        return False

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # create the adjacency list

        adj = defaultdict(list)
        n = len(stones)
        dsu = DisjointSet(n, stones)
        for i in range(n):
            source_x, source_y = stones[i]
            for j in range(n):
                if i != j:
                    if source_x == stones[j][0] or source_y == stones[j][1]:
                        adj[tuple(stones[i])].append(tuple(stones[j]))
        res = 0
        for key in adj.keys():
            for nbor in adj[key]:
                if dsu.same_parent(key, nbor):
                    continue
                else:
                    dsu.unite(key, nbor)
                    res += 1
        return res


        
        