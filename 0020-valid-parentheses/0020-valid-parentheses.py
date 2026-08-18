class Solution:
    def isValid(self, s: str) -> bool:
        seen = {'(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in seen:
                stack.append(ch)
            elif ch in seen.values():
                if not stack:
                    return False
                elif ch == seen[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack
