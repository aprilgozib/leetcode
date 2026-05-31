class Solution:
    def firstUniqChar(self, s: str) -> int:
        # use dictionary
        seen = {} # l:1, e:3, t:1
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        
        for index, value in enumerate(s):
            if seen[value] == 1:
                return index
        
        return -1
