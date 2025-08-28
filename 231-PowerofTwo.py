'''
Problem Name: 231. Power of Two
Attempted : # 29-08-2025
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
