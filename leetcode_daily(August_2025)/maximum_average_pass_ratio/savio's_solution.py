import heapq
from typing import List 

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        def change_in_pass_ratio(passes, total):
            return ((passes + 1) / (total + 1)) - passes / total

        hp = []

        for passes, total in classes:
            change = change_in_pass_ratio(passes, total)
            heapq.heappush(hp, (-change, passes, total))
        
        while extraStudents > 0:
            change, passes, total = heapq.heappop(hp)
            nw_change = change_in_pass_ratio(passes + 1, total + 1)
            heapq.heappush(hp, (-nw_change, passes + 1, total + 1))
            extraStudents -= 1

        total_pass_ratio = sum(
            passes / total_students for _, passes, total_students in hp
        )

        return total_pass_ratio / n
            

        

