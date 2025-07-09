'''
Problem Name: 3439. Reschedule Meetings for Maximum Free Time I
Attempted : # 10-07-2025
'''

shouldprint = True 

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        nums = [startTime[0]]
        for i in range(1, len(endTime)):
            nums.append(startTime[i] - endTime[i - 1])
        nums.append(eventTime - endTime[-1])
        ans = s = 0
        print("nums,s",nums,s)
        for i, x in enumerate(nums):
            s += x
            print("s",s)
            if i >= k:
                ans = max(ans, s)
                s -= nums[i - k]
                print(s,i,k,nums[i-k],"\n")
        return ans


        # gaps = []
        # startTime = startTime + [eventTime]
        # endTime = [0] + endTime
        # n = len(startTime)
        # for j in range(n):
        #     gaps.append(startTime[j] - endTime[j])
        # if shouldprint: print("\n\nInitial gaps => ",gaps)

        # maxAns = 0
        # for i in range(len(gaps) - k):
        #     # print(gaps[i:i+k+1])
        #     maxAns = max(maxAns,sum(gaps[i:i+k+1]))
        # return maxAns

    


s = Solution()

# print(s.maxFreeTime(5,1,[1,3],[2,5]))
# print(s.maxFreeTime(10,1,[0,2,9],[1,4,10]))
# print(s.maxFreeTime(5,2,[0,1,2,3,4],[1,2,3,4,5]))
# print(s.maxFreeTime(21,1,[7,10,16],[10,14,18]))
# print(s.maxFreeTime(34,2,[0,17],[14,19]))
# print(s.maxFreeTime(17,3,[7,12,15],[12,14,17]))
# print(s.maxFreeTime(482,2,[21,67,151,448],[23,132,219,449]))
# print(s.maxFreeTime(227,3,[12,16,215,222],[14,201,219,225]))
# print(s.maxFreeTime(13,4,[0,2,3,6,11],[2,3,4,11,12]))
# print(s.maxFreeTime(22,4,[0,2,7,10,11,15],[1,5,10,11,15,20]))
print(s.maxFreeTime(263,3,[56,60,151,173,253,257],[58,83,161,249,256,263]))