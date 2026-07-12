class Solution:
    def isValid(self, s: str) -> bool:
        seen = {'(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in seen: # open
                stack.append(ch)
            elif ch in seen.values(): # close
                if not stack:
                    return False
                elif ch == seen[stack[-1]]: # match
                    stack.pop()
                else:
                    return False
        return not stack