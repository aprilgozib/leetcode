class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        for ch in t:
            #if ch not in seen:
            if ch in seen and seen[ch] > 0:
                seen[ch] -= 1
            else:
                return ch