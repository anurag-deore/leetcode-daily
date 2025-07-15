'''
Problem Name: 2200. Find All K-Distant Indices in an Array
Attempted : # 15-07-2025
'''

class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        keyIndexes = []
        finalList = []
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == key:
                keyIndexes.append(i)
                beforeStart = 0 if i - k < 0 else i - k
                beforeEnd =  n if (i+2) + k > n else i+1+k
                finalList.extend(list(range(beforeStart,beforeEnd)))
              
        return list(set(finalList))

s = Solution()
print(s.findKDistantIndices([3,4,9,1,3,9,5], 9, 1))     
print(s.findKDistantIndices([2,2,2,2,2],2,2))     
print(s.findKDistantIndices([1,2,3,4,5,6,7,8,9,10],2,5))     