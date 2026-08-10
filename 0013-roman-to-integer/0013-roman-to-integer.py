class Solution:
    def romanToInt(self, s: str) -> int:
        seen = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s) - 1):
            if seen[s[i]] < seen[s[i + 1]]:
                res -= seen[s[i]]
            else:
                res += seen[s[i]]
        res += seen[s[-1]]
        return res
            