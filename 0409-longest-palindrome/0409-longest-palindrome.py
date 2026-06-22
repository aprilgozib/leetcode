class Solution:
    def longestPalindrome(self, s: str) -> int:
        # even number -> use all
        # odd number -> use even number of character
        # at least one odd number of character -> add on middle
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        result = 0
        has_odd = False

        for cnt in seen.values():
            result += cnt // 2 * 2 # only even
            if cnt % 2 == 1: # odd
                has_odd = True

        if has_odd:
            result += 1

        return result