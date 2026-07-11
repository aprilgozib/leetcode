class Solution:
    def longestPalindrome(self, s: str) -> int:
        # add all even, odd - 1
        # if odd + 1
        seen = {}
        is_odd = False
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        res = 0
        for count in seen.values():
            res += count // 2 * 2
            if count % 2 == 1: #odd
                is_odd = True
            
        if is_odd:
            return res + 1
        else:
            return res
