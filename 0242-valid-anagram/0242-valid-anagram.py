class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        
        for ch in t:
            if ch in seen:
                seen[ch] -= 1
            else: # ch not in seen
                return False
        
        for count in seen.values():
            if count != 0: # count should be zero
                return False

        return True

        