from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf_arr = [float("inf") for _ in range(n + 1)]
        inf_arr[k] = 0
        adj_list = defaultdict(list)

        for u, v, w in times:
            adj_list[u].append((v, w))

        hp = []
        heapq.heappush(hp, (0, k))

        while hp:
            time, node = heapq.heappop(hp)

            for nbor in adj_list[node]:
                n_node, n_time = nbor
                c_time = time + n_time 
                if c_time < inf_arr[n_node]:
                    inf_arr[n_node] = c_time
                    heapq.heappush(hp, (c_time, n_node))
        main_res = inf_arr[1:]
        if float("inf") in main_res:
            return -1
        return max(main_res)
                
        

        