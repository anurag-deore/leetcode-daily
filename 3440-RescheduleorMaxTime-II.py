'''
Problem Name: 3440. Reschedule Meetings for Maximum Free Time II
Attempted : # 11-07-2025
'''

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        gaps = []
        p=0
        n = len(startTime)
        for j in range(n):
            gaps.append(startTime[j] - p)
            p = endTime[j]
        gaps.append(eventTime - p)
        # print("\n\nInitial gaps => ",gaps)
        maxAns = 0
        for i in range(len(gaps)-1):
            maxAns = max(maxAns,gaps[i]+gaps[i+1])
        # print(maxAns)

        num_gaps = len(gaps)
        prefix_max_gaps = [0] * num_gaps
        prefix_max_gaps[0] = gaps[0]
        for i in range(1, num_gaps):
            prefix_max_gaps[i] = max(prefix_max_gaps[i - 1], gaps[i])

        suffix_max_gaps = [0] * num_gaps
        suffix_max_gaps[num_gaps - 1] = gaps[num_gaps - 1]
        for i in range(num_gaps - 2, -1, -1):
            suffix_max_gaps[i] = max(suffix_max_gaps[i + 1], gaps[i])

        print(prefix_max_gaps)
        print(suffix_max_gaps)

        for i in range(n):
            dur = endTime[i] - startTime[i]
            can_move = False
            # Check for a slot in the gaps to the left
            if i > 0 and prefix_max_gaps[i - 1] >= dur:
                can_move = True
            # Check for a slot in the gaps to the right
            if not can_move and i + 2 < num_gaps and suffix_max_gaps[i + 2] >= dur:
                can_move = True

            if can_move:
                maxAns = max(maxAns,  gaps[i] + dur + gaps[i + 1])
            # print("\nindex = ",i,"\n",dur,gaps[0:i],gaps[i+2:],"=> ",gaps[i],"+",gaps[i+1],"+",dur,"=",gaps[i]+gaps[i+1]+dur)
        return maxAns


s = Solution()

print(s.maxFreeTime(41,[17,24],[19,25]))
# print(s.maxFreeTime(15,[1,3,6,9,12],[2,4,8,12,13]))
# print(s.maxFreeTime(10,[0,3,7,9],[1,4,8,10]))
# print(s.maxFreeTime(5,[1,3],[2,5]))
# print(s.maxFreeTime(10,[0,7,9],[1,8,10]))
# print(s.maxFreeTime(5,[0,1,2,3,4],[1,2,3,4,5]))
# print(s.maxFreeTime(21,[7,10,16],[10,14,18]))
# print(s.maxFreeTime(34,[0,17],[14,19]))
# print(s.maxFreeTime(17,[7,12,15],[12,14,17]))
# print(s.maxFreeTime(482,[21,67,151,448],[23,132,219,449]))
# print(s.maxFreeTime(227,[12,16,215,222],[14,201,219,225]))
# print(s.maxFreeTime(13,[0,2,3,6,11],[2,3,4,11,12]))
# print(s.maxFreeTime(22,[0,2,7,10,11,15],[1,5,10,11,15,20]))
# print(s.maxFreeTime(263,[56,60,151,173,253,257],[58,83,161,249,256,263]))