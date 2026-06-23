class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f_max = float('-inf')
        s_max = float('-inf')
        t_max = float('-inf')
        for i in nums:
            if i == f_max or i == s_max or i == t_max:  # skip duplicate
                continue
            if i > f_max:
                t_max = s_max
                s_max = f_max
                f_max = i
            elif i < f_max and i > s_max:
                t_max = s_max
                s_max = i
            elif i < s_max and i > t_max:
                t_max = i
        return t_max if t_max != float('-inf') else f_max