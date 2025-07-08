'''
Problem Name: 1751. Maximum Number of Events That Can Be Attended II
Attempted : # 08-07-2025
'''
from functools import cache
from bisect import bisect_right

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
      n = len(events)
      events.sort()
      starts = [s for s,_,_ in events]
      
      @cache
      def dp(i, count):
        if i == n or count == 0: return 0
        next = bisect_right(starts, events[i][1])
        return max(dp(i+1, count), dp(next, count - 1) + events[i][2])
      return dp(0, k)
 

s = Solution()
print(s.maxValue([[1,2,4],[3,4,3],[2,3,10]],2))