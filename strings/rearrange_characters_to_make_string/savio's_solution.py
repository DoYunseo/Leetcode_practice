from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count_s = Counter(s)
        count_tg = Counter(target)
        max_list = []
        for key, val in count_tg.items():
            if key in count_s:
                # applying bottleneck principle
                max_list.append(count_s[key] // val)
            elif key not in count_s:
                return 0
        return min(max_list) 
    