'''
Problem Name: 1394. Find Lucky Integer in an Array
Attempted : # 06-07-2025
'''

def findLucky(arr: list[int]) -> int:
    luckyArr = {}
    luckyInt = -1
    for i in arr:
        if luckyArr.get(i) == None:
            luckyArr[i] = 1
        else:
            luckyArr[i] += 1
    for index,j in enumerate(luckyArr):
        if j == luckyArr[j]:
            luckyInt = max(luckyInt,j)
    return luckyInt


print(findLucky([2,2,3,4]))