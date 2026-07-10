class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        for ch in t:
            if ch not in seen:
                return False
            else:
                seen[ch] -= 1
                
        for value in seen.values():
            if value > 0:
                return False
            elif value < 0:
                return False

        return True