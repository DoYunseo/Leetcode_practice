class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        track_count = 0

        for c in s:
            if track_count >= 2 and stack and stack[-1] == c:
                track_count += 1
                continue
            elif stack and stack[-1] != c:
                track_count = 1
            else:
                track_count += 1
            stack.append(c)
        return "".join(stack)
