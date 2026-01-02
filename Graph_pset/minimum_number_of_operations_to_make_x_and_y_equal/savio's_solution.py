class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        steps = 0
        dq = deque([x])
        visited = set([x])

        while dq:
            n = len(dq)
            for _ in range(n):
                curr = dq.popleft()

                if curr == y:
                    return steps
                if curr % 11 == 0:
                    nextval = curr // 11
                    if nextval not in visited:
                        visited.add(nextval)
                        dq.append(nextval)
                if curr % 5 == 0:
                    nextval = curr // 5
                    if nextval not in visited:
                        visited.add(nextval)
                        dq.append(nextval)
                
                nextval = curr + 1
                if nextval not in visited:
                    visited.add(nextval)
                    dq.append(nextval)
                
                nextval = curr - 1
                if nextval > 0 and nextval not in visited:
                    visited.add(nextval)
                    dq.append(nextval)
            steps += 1