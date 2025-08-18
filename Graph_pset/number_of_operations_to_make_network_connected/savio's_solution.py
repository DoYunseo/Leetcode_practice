from typing import List

class DisjointSet():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find_ulp(self, node):
        if node == self.parent[node]:
            return node
        else:
            self.parent[node] = self.find_ulp(self.parent[node])
            return self.parent[node]

    def union_rank(self, node1, node2):
        rankA, rankB = self.rank[self.find_ulp(node1)], self.rank[self.find_ulp(node2)]

        if rankA == rankB:
            self.parent[self.find_ulp(node1)] = self.find_ulp(node2)
            self.rank[self.find_ulp(node2)] += 1 

        elif rankA > rankB:
            self.parent[self.find_ulp(node2)] = self.find_ulp(node1)
        else:
            self.parent[self.find_ulp(node1)] = self.find_ulp(node2)
    def same_parent(self, nodeA, nodeB):
        
        if self.find_ulp(nodeA) == self.find_ulp(nodeB):
            return True
        else:
            return False
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        n_connection = len(connections)
        if n_connection + 1 < n:
            return -1

        union = DisjointSet(n)
        for u, v in connections:
            if union.same_parent(u, v):
                continue
            else:
                union.union_rank(u, v)
        components = len(set(union.find_ulp(i) for i in range(n)))
        return components - 1
        


        
        