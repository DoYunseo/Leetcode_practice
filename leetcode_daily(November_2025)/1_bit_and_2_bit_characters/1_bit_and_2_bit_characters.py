class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        stack = []
        i, n = 0, len(bits)
        while i < n:
            if bits[i] == 0:
                stack.append("0")
                i += 1
            else:
                token = "1" + str(bits[i + 1])
                stack.append(token)
                i += 2
        return stack[-1] == "0"
