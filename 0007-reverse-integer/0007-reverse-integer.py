class Solution:
    def reverse(self, x: int) -> int:
        # sign
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)

        res = 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31 - 1

        while x > 0:
            digit = x % 10 # 3 -> 2 -> 1
            res = res * 10 + digit # 0 * 10 + 3 -> 3 * 10 + 2 -> 32 * 10 + 1
            x //= 10 # 12 -> 1 -> 0

        res *= sign
        if res < INT_MIN or res > INT_MAX:
            return 0
        return res