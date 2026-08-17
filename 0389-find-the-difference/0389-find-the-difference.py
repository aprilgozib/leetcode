class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        for ch in t:
            if ch not in seen or seen[ch] < 1:
                return ch
            seen[ch] -= 1

        