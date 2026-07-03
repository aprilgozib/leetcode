class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        for ch in t:
            if ch not in seen:
                return False
            elif seen[ch] < 0:
                return False
            else:
                seen[ch] -= 1
        for count in seen.values():
            if count != 0:
                return False
        return True