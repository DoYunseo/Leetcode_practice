class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        save_sign = -1
        is_less = False
        if num == 0:
            return "0"
        if num < 0:
            num = num * save_sign
            is_less = True

        while num > 0:
            res += str(num % 7)
            num = num // 7
        if is_less:
            res += "-"
            return res[::-1]
        else:
            return res[::-1]
        