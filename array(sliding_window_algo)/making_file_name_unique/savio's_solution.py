from typing import List
from collections import defaultdict

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        hmap = defaultdict(int)
        res = []

        for name in names:
            if name not in hmap:
                res.append(name)
                hmap[name] = 0
            else:
                hmap[name] += 1
                counter = hmap[name]
                while True:
                    new_name = f"{name}({counter})"
                    if new_name not in hmap:
                        res.append(new_name)
                        hmap[new_name] = 0
                        break
                    else:
                        counter += 1
        return res