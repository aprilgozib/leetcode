class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use two pointer
        # use dictionary
        left = 0
        seen = {}
        res = 0
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left: # move duplicate
                left = seen[ch] + 1
            seen[ch] = right
            res = max(res, right - left + 1)
        return res