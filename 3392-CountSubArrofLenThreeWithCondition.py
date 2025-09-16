'''
Problem Name : 3392. Count Subarrays of Length Three With a Condition
Attempted : # 17-09-2025
'''
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if 2 * (a + c) == b:
                count += 1
        return count
