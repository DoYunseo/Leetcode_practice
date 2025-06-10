class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = [char for char in s]
        print(s)
        n = len(s)
        start, end = 0, n - 1
        moves = 0

        while start < end:
            k = end
            while k > start:
                if s[k] == s[start]: #match has been found:
                    #now move k until you get to end
                    for m in range(k, end):
                        s[m], s[m + 1] = s[m + 1], s[m]
                        moves += 1
                    end -= 1
                    break
                k -= 1
            if k == start:
                moves += n // 2 - start

            start += 1
        return moves
        