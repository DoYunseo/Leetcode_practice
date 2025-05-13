# First solution: Time limit
#
#  class Solution:
#     def lengthAfterTransformations(self, s: str, t: int) -> int:
#         for _ in range(t):
#             arr = []
#             for i in range(len(s)):
#                 if s[i] == "z":
#                     arr.append("ab")
#                 else:
#                     arr.append(chr(ord(s[i]) + 1))
#             s = ''.join(arr)

#         return len(s) % (10**9 + 7)

# Second approach -> dynamic programming
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (t + 1) for _ in range(26)]

        # initial state
        for c in range(26):
            dp[c][0] = 1

        # transformation t times
        for i in range(1, t + 1):
            for c in range(26):
                if c == 25:  # 'z'
                    dp[c][i] = (dp[0][i - 1] + dp[1][i - 1]) % MOD  # 'z' → 'a' + 'b'
                else:
                    dp[c][i] = dp[c + 1][i - 1]  # 'e' → 'f'

        result = 0
        for ch in s:
            result = (result + dp[ord(ch) - ord('a')][t]) % MOD
        return result