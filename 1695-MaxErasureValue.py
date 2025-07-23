'''
Problem Name: 1695. Maximum Erasure Value
Attempted : # 23-07-2025
'''
import time

class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    

s = Solution()
# print(s.maximumUniqueSubarray([4,2,4,5,6]))
# print(s.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
print(s.maximumUniqueSubarray([10000,1,10000,1,1,1,1,1,1]))