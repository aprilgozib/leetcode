class Solution:
    def reverse(self, x: int) -> int:
        # thinking about digit and reverse
        if x < 0:
            sign = -1
        else:
            sign = 1
        
        x = abs(x)

        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while x > 0:
            digit = x % 10  # 3
            res = res * 10 + digit # 0*10 + 3 = 3
            x //= 10 # 12

        res *= sign

        if res < INT_MIN or res > INT_MAX:
            return 0

        return res