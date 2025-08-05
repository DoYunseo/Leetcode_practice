import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))  # u -> v with cost w

        INF = 1e9
        min_heap = [(0, src, 0)]  #(cost, node, stops) 
        visited = dict()
        
        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)

            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            if (node, stops) in visited and visited[(node, stops)] <= cost:
                continue
            
            visited[(node, stops)] = cost

            for nei, price in graph[node]:
                heapq.heappush(min_heap, (cost + price, nei, stops + 1))
                
        return -1