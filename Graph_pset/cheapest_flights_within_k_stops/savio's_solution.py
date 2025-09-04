from collections import defaultdict
from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

        hp = []
        relax = [float('inf') for i in range(n)]
        relax[src] = 0

        heapq.heappush(hp, (0, 0, src))

        while hp:
            stops, cost, pos = heapq.heappop(hp)
            for nbor in adj_list[pos]:
                new_v, n_cost = nbor
                calc_nw = n_cost + cost
                if calc_nw < relax[new_v] and stops < k + 1:
                    relax[new_v] = calc_nw
                    heapq.heappush(hp, (stops + 1, calc_nw, new_v))
        return relax[dst] if relax[dst] != float("inf") else -1

        