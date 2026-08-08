class Solution:
    def longestPalindrome(self, s: str) -> int:
        # count characters
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        # {a:1, b:1, c:4, d:2}
        # add all even, odd - 1
        # if odd is there + 1
        res = 0
        is_odd = False
        for count in seen.values():
            res += count // 2 * 2
            if count % 2 == 1: # odd
                is_odd = True
        
        if is_odd:
            return res + 1
        else:
            return res
        