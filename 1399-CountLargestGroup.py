'''
Problem Name: 1399. Count Largest Group
Attempted : # 15-07-2025
'''
import pprint

class Solution:
    def countLargestGroup(self, n: int) -> int:
        pretty = pprint.PrettyPrinter(width=30)
        countMap = {}
        maxCount = [0,0] # [count,occurences]
        for i in range(1,n+1):
            sumDigits = 0
            if(i > 9):
              num = list(str(i))
              sumDigits += sum(map(lambda x:int(x),num))
            else:
              sumDigits += i

            if countMap.get(sumDigits) == None:
                countMap[sumDigits] = [i]
            else:
               countMap[sumDigits].append(i)
            pretty.pprint(countMap[sumDigits])
           
            if maxCount[0] < len(countMap[sumDigits]):
               maxCount[0] = len(countMap[sumDigits])
               maxCount[1] = 1
            elif maxCount[0] == len(countMap[sumDigits]):
               maxCount[1] += 1
            print(f"{maxCount} => maxCount, {i} => i\n\n")
        return maxCount[1]

s = Solution()
print(s.countLargestGroup(46))
# # print(s.countLargestGroup(13))
# print(s.countLargestGroup(2))