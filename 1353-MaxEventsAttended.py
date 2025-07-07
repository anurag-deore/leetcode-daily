'''
Problem Name: 1353. Maximum Number of Events That Can Be Attended
Attempted : # 07-07-2025
'''
import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
      events.sort()

      attended_events = 0  
      day = 0      
      event_idx = 0  
      min_heap = [] 
      while event_idx < len(events) or min_heap:
          if not min_heap and event_idx < len(events):
              day = max(day, events[event_idx][0]) 
          while event_idx < len(events) and events[event_idx][0] <= day:
              heapq.heappush(min_heap, events[event_idx][1]) 
              event_idx += 1
          while min_heap and min_heap[0] < day:
              heapq.heappop(min_heap)
          if min_heap:
              heapq.heappop(min_heap)  
              attended_events += 1     
              day += 1                

      return attended_events
    
s = Solution()

print(s.maxEvents([[1,2],[2,3],[3,4],[1,2]]))
# print(s.maxEvents([[1,2],[2,3],[3,4]]))
print(s.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]]))
print(s.maxEvents([[1,2],[2,2],[3,3],[3,4],[3,4]]))