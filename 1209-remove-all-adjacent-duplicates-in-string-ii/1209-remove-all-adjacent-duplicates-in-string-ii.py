class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # use stack 2 dimension
        #[[a,1],[b,1],[c,1]]
        stack = []
        for ch in s:
            if not stack:
                stack.append([ch, 1])
            elif stack[-1][0] == ch: # same alphabet
                stack[-1][1] += 1
            else: # different
                stack.append([ch, 1])

            if stack[-1][1] == k:
                stack.pop()

        res = []
        for ch, count in stack:
            res.append(ch * count)

        return ''.join(res)