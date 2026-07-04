class Solution:
    def longestPalindrome(self, s: str) -> int:
        # even number -> use all
        # odd number -> use -1
        # if odd number -> add one middle
        seen ={}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        
        has_odd = False
        res = 0

        for count in seen.values():
            res += count // 2 * 2
            if count % 2 == 1: # odd
                has_odd = True
        
        if has_odd:
            res += 1
        
        return res