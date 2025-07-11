'''
Problem Name: 2402. Meeting Rooms III
Attempted : # 12-07-2025
'''
from heapq import heapify,heappop,heappush

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        busy = []
        idle = list(range(n))
        heapify(idle)
        cnt = [0] * n
        for s, e in meetings:
            while busy and busy[0][0] <= s:
                heappush(idle, heappop(busy)[1])
            if idle:
                i = heappop(idle)
                cnt[i] += 1
                heappush(busy, (e, i))
            else:
                a, i = heappop(busy)
                cnt[i] += 1
                heappush(busy, (a + e - s, i))
        ans = 0
        for i, v in enumerate(cnt):
            if cnt[ans] < v:
                ans = i
        return ans



s = Solution()
# print(s.mostBooked(2,[[0,10],[1,5],[2,7],[3,4]]))
print(s.mostBooked(3,[[1,20],[2,10],[3,5],[4,9],[6,8]]))