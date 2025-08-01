'''
Problem Name: 3396. Minimum Number Of Operations to Make Elements in Array Distinct
Attempted : # 01-08-2025
'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def helper(arr, ops):
            if len(arr) <= 1 or len(arr) == len(set(arr)):
                return ops
            return helper(arr[3:], ops + 1)

        return helper(nums, 0)
