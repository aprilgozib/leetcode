class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonachi
        # n = 1 -> 1
        # n = 2 -> 1,1 2
        # n = 3 -> 1,1,1 1,2 2,1 
        # n = 4 -> 1,1,1,1 1,1,2 1,2,1 2,1,1 2,2
        # f(n) = f(n-2) + f(n-1)
        if n <= 2:
            return n
        
        prev2, prev1 = 1, 2
        for i in range(3, n+1):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr
        return prev1