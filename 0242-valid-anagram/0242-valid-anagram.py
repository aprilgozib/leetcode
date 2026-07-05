class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        
        for ch in t:
            if ch not in seen or seen[ch] < 0:
                return False
            seen[ch] -= 1
        
        for count in seen.values():
            if count > 0:
                return False
        
        return True