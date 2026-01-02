class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        for n in permutations(s):
            jo = "".join(list(n))
            if jo[0] != "0":
                num = int(jo)
                if num & num - 1 == 0:
                    return True
        return False

