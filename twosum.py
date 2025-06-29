# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        c = target - nums[i]
        if c in d:
            return d[c], i
        d[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
