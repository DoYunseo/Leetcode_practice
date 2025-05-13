class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        #change to array
        #first approach was theoretically correct but it hit TLE
        # spl_arr = [char for char in s]

        # while t > 0:
        #     for i in range(len(spl_arr)):
        #         if spl_arr[i] == "z":
        #             spl_arr[i] = "ab"
        #             continue
        #         spl_arr[i] = chr(ord(spl_arr[i]) + 1)
        #     spl_arr = [char for char in "".join(spl_arr)]
        #     t -= 1
        # return len(spl_arr) % 10**9 + 7

        #second approach

        alpha_count = [0] * 26
        MOD = 10**9 + 7
        n = len(s)
        for i in range(n):
            chr_pos = ord(s[i]) - 97
            alpha_count[chr_pos] += 1
        
        while t > 0:
            z_count = alpha_count[25]

            for i in range(len(alpha_count) - 1, 0, -1):
                alpha_count[i] = alpha_count[i - 1] % MOD
                alpha_count[i - 1] = 0
            alpha_count[0] = (alpha_count[0] + z_count) % MOD
            alpha_count[1] = (alpha_count[1] + z_count) % MOD
            t -= 1
        return sum(alpha_count) % MOD

