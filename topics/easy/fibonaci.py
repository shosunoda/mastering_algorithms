class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def helper(n):
            if n <=1:
                return n
            if n in cache:
                return cache[n]
            cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
        return helper(n)
            