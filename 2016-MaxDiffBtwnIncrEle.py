'''
Problem Name: 2016. Maximum Difference Between Increasing Elements
Attempted : # 31-08-2025
'''

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = float('inf')
        max_diff = -1
        for num in nums:
            if num > min_val:
                 max_diff = max(max_diff, num - min_val)
            else:
                min_val = num
        return max_diff
