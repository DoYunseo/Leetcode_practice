class Solution:
    def minPartitions(self, n: str) -> int:
        m = 1
        for i in range(len(n)):
            no = int(n[i])
            if no > m:
                m = no
        return m
