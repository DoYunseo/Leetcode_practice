from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [str(i) for i in range(1, n + 1)]
        return [int(x) for x in sorted(res)]

