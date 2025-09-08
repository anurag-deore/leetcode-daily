'''
Problem Name : 1317. Convert Integer to the Sum of Two No-Zero Integers
Attempted : # 08-09-2025
'''

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:    
        def has_zero(num):
            return '0' in str(num)
        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]
