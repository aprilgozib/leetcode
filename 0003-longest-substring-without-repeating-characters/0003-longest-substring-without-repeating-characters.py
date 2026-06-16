class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using two pointer
        left = 0
        seen = {}
        res = 0
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left: # duplicate
                left = seen[ch] + 1
            seen[ch] = right
            res = max(res, right - left + 1)

        return res