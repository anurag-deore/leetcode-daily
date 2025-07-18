'''
Problem Name: 2163. Minimum Difference in Sums After Removal of Elements
'''
import heapq
import math

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
      n = len(nums) // 3
      prefix_min_sum = [0] * (3 * n)
      suffix_max_sum = [0] * (3 * n)

      current_sum = 0
      max_heap = []  

      for i in range(3 * n):
          current_sum += nums[i]
          heapq.heappush(max_heap, -nums[i])

          if len(max_heap) > n:
              largest_element = -heapq.heappop(max_heap)
              current_sum -= largest_element
          
          if len(max_heap) == n:
              prefix_min_sum[i] = current_sum

      current_sum = 0
      min_heap = []

      for i in range(3 * n - 1, -1, -1):
          current_sum += nums[i]
          heapq.heappush(min_heap, nums[i])

          if len(min_heap) > n:
              smallest_element = heapq.heappop(min_heap)
              current_sum -= smallest_element
          
          if len(min_heap) == n:
              suffix_max_sum[i] = current_sum
        
      min_diff = math.inf

      for i in range(n - 1, 2 * n):
          sumfirst = prefix_min_sum[i]
          sumsecond = suffix_max_sum[i + 1]
          min_diff = min(min_diff, sumfirst - sumsecond)
          
      return min_diff
    

s = Solution()
print(s.minimumDifference([7,9,5,8,1,3]))