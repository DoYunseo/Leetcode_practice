class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1 
        
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            return parent[x]
        
        def union(a,b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True
        
        components = n  
        for a, b in connections:
            if union(a, b):
                components -= 1
        
        return components - 1
        
