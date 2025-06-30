'''
Problem Name: 594. Longest Harmonious Subsequence
Attempted : # 30-06-2025
'''


def findLHS(nums: list[int]) -> int:
    res = 0
    countmap = {}
    for i in nums:
        if(countmap.get(i) == None):
            countmap[i] = 1
        else:
            countmap[i] += 1

    for i in nums:
        minNum = i
        maxNum = i+1
        if(countmap.get(maxNum)):
            res = max(res,countmap.get(minNum)+countmap.get(maxNum))
    return res
print(findLHS([1,1,1,1]))