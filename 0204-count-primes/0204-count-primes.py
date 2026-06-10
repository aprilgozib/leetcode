class Solution:
    def countPrimes(self, n: int) -> int:
        # F, T list checking
        if n < 2:
            return 0
        
        is_prime = [True] * n # [T, T, T, T, T...]
        is_prime[0] = False
        is_prime[1] = False # [F, F, T, T, T, T...]

        for i in range(2, n):
            if is_prime[i]: # True
                for j in range(i*i, n, i): # i*i is point
                    is_prime[j] = False
        
        return sum(is_prime)

