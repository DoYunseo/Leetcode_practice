class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        adj = defaultdict(list)

        for u, v in tickets:
            adj[u].append(v)
            outdeg[u] += 1
            indeg[v] += 1
        
        print(adj)

        for v in adj:
            adj[v].sort(reverse=True)
        
        print(adj)

        stack = ["JFK"]
        circuit = []

        while stack:
            v = stack[-1]
            if adj[v]:
                stack.append(adj[v].pop())   # walk down an unused edge
            else:
                circuit.append(stack.pop())  # dead end -> settle onto the tail
        circuit.reverse()

        return circuit

    



        # so the tree is rooted at JFK


        