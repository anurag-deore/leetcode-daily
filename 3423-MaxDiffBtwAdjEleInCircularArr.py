'''
Problem Name: 3423. Maximum Difference Between Adjacent Elements in a Circular Array 
Attempted : # 30-08-2025
'''

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[i] - nums[i - 1])
                for i in range(len(nums)))
