'''
Problem Name: 2210. Count Hills and Valleys in an Array
Attempted : # 27-07-2025
'''


class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        prev = 0
        next = 1 if len(nums) > 0 else 0
        i = 0
        hv = 0
        while next < len(nums):
            # print(i, "=>", prev, nums[i], next)
            if i == 0:
                i += 1
                prev = i - 1
                # print("first\n")
            elif nums[i] == nums[next] or nums[i] == nums[prev]:
                # print("same\n")
                i += 1
            elif (nums[prev] < nums[i] and nums[i] > nums[next]) or (nums[prev] > nums[i] and nums[i] < nums[next]):
                # print("hill or valley\n")
                hv += 1
                i += 1
                prev = i - 1
            else:
                i += 1
            next += 1
            # print("hv => ", hv, "\n")
            # time.sleep(0.5)
        return hv


s = Solution()
print(s.countHillValley([2, 4, 1, 1, 6, 5]))
print(s.countHillValley([1, 4, 2, 2, 6, 5]))
print(s.countHillValley([35, 29, 9, 63, 32, 9, 57,
      78, 47, 99, 59, 49, 88, 1, 27, 51, 73, 92]))
print(s.countHillValley([6, 6, 5, 5, 4, 1]))
# print(s.countHillValley([6, 5, 6]))
# print(s.countHillValley([6]))
# print(s.countHillValley([6, 5]))
