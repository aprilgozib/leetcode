class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        res = 0
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left: # move duplicate
                left = seen[ch] + 1
            seen[ch] = right
            res = max(res, right - left + 1)
        return res