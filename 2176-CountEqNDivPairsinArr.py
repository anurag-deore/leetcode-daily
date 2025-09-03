'''
Problem Name : 2176. Count Equal and Divisible Pairs in an Array
Attempted : # 03-09-2025
'''


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    counter += 1

        return counter
