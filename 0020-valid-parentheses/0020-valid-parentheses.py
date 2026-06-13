class Solution:
    def isValid(self, s: str) -> bool:
        seen = {'(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in seen: # open
                stack.append(ch)
            else: # close
                if not stack or seen[stack[-1]] != ch:
                    return False
                stack.pop()
        return not stack
