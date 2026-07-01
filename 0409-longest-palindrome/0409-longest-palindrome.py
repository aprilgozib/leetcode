class Solution:
    def longestPalindrome(self, s: str) -> int:
        # even number -> use all
        # odd number -> use - 1
        # at least one odd number of character -> add on middle
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        
        result = 0
        has_odd = False
        
        for count in seen.values():
            result += count // 2 * 2 # use only even
            if count % 2 == 1: # odd
                has_odd = True
        
        if has_odd:
            result += 1
        
        return result