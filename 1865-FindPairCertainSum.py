'''
Problem Name: 1865. Finding Pairs With a Certain Sum
Attempted : # 06-07-2025
'''
from collections import Counter

class FindSumPairs:
    nums1 = []
    nums2 = []
    num2map= {}
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.num2map = Counter(self.nums2)
        return

    def add(self, index: int, val: int) -> None:
        self.num2map[self.nums2[index]] -= 1
        self.nums2[index] += val 
        self.num2map[self.nums2[index]] += 1
        return self.nums2
        

    def count(self, tot: int) -> int:
        pairs = 0
        for key in self.nums1:
            diff = tot - key
            if self.num2map[diff] != None:
                 pairs += self.num2map[diff]
        return pairs
        


findSumPairs = FindSumPairs([1,1,2,2,2,3],[1,4,5,2,5,4])
for i in range(55):
    findSumPairs.add(1,100000)

print(findSumPairs.count(1))