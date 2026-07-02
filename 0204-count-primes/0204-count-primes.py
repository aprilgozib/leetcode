class Solution:
    def countPrimes(self, n: int) -> int:
        # F, T mark
        # i*i, n, i # 배수
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, n):
            if is_prime:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        return sum(is_prime)