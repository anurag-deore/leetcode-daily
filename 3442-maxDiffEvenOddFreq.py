'''
    Problem Name: 3442. Maximum Difference Between Even and Odd Frequency I
    Attempted : # 24-08-2025
    '''

from collections import Counter
import math


class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s).values()
        a1 = math.inf  # even
        a2 = 0  # odd
        for j in counts:
            if (j % 2 == 0):
                a1 = min(a1, j)
            else:
                a2 = max(a2, j)
        return a2-a1


s = Solution()
print(s.maxDifference("aaaaabbc"))
print(s.maxDifference("abcabcab"))
