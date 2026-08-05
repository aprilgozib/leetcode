class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f_max = float('-inf')
        s_max = float('-inf')
        t_max = float('-inf')

        for num in nums:
            if num == f_max or num == s_max or num == t_max:
                continue

            if num > f_max:
                t_max = s_max
                s_max = f_max
                f_max = num
            elif num < f_max and num > s_max:
                t_max = s_max
                s_max = num
            elif num < s_max and num > t_max:
                t_max = num

        if t_max == float('-inf'):
            return f_max
        else:
            return t_max