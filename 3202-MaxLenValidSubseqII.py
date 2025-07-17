'''
Problem Name: 3202. Find the Maximum Length of Valid Subsequence II
Attempted : # 18-07-2025
'''

from collections import defaultdict
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
      dp = [[0] * k for _ in range(k)]
      for x in nums:
        for y in range(k):
          dp[x % k][y] = dp[y][x % k] + 1

      return max(map(max, dp))

s = Solution()
print(s.maximumLength([1,4,2,3,1,4], 3))
print(s.maximumLength([5,3,9],6))