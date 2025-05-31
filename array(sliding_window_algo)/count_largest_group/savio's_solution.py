from collections import defaultdict
 
class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = defaultdict(int)
        for i in range(1, n + 1):
            s = str(i)
            if len(s) > 1:
                nw = [int(char) for char in s]
                count[sum(nw)] += 1
            else:
                count[int(s)] += 1
        max_count = max([val for val in count.values()])
        co_lst = 0

        for key, val in count.items():
            if val == max_count:
                co_lst += 1
        return co_lst
            