class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        if len(v1) < len(v2):
            d = abs(len(v2) - len(v1))
            v1 = v1 + ["0"] * d
        elif len(v1) > len(v2):
            d = abs(len(v2) - len(v1))
            v2 = v2 + ["0"] * d

        ptr1, ptr2 = 0, 0

        while ptr1 < len(v1) and ptr2 < len(v2):
            if int(v1[ptr1]) > int(v2[ptr2]):
                return 1
            elif int(v1[ptr1]) < int(v2[ptr2]):
                return -1
            ptr1 += 1
            ptr2 += 1
        return 0
