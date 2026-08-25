class Solution:
    def isValid(self, s: str) -> bool:
        seen = {'(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in seen: # open
                stack.append(ch)
            elif ch in seen.values(): # close
                if not stack: # empty
                    return False
                elif ch == seen[stack[-1]]: # match
                    stack.pop()
                else: # not match
                    return False

        return not stack # stack should be empty