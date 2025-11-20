class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        todo = [2] * n
        ans = 0

        for i in range(n - 1, -1, -1):
            s, e = intervals[i]
            t = todo[i]
            if t <= 0:
                continue
            # pick t numbers: s, s+1, ...
            for p in range(s, s + t):
                ans += 1
                # reduce future todos
                for j in range(i):
                    s0, e0 = intervals[j]
                    if todo[j] > 0 and s0 <= p <= e0:
                        todo[j] -= 1
        return ans