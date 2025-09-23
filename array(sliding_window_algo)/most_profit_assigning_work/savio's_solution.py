from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # map worker to job
        jobs = sorted(zip(difficulty, profit))
        max_profits = []
        current_max = 0

        for d, p in jobs:
            current_max = max(current_max, p)
            max_profits.append((d, current_max))
        print(max_profits)

        running_total = 0
        for w in worker:
            left, right = 0, len(max_profits) - 1
            best_idx = -1
            while left <= right:
                mid = left + (right - left) // 2
                d = max_profits[mid][0]
                if d <= w:
                    best_idx = mid
                    left = mid + 1
                elif d > w:
                    right = mid - 1
            if best_idx != -1:
                running_total += max_profits[best_idx][1]
        return running_total
