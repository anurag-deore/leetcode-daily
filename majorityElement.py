# https://leetcode.com/problems/majority-element/
'''
'''


def majorityElement(nums):
    o = {}
    for i in nums:
        o[i] = o.get(i, 0) + 1
    for num in nums:
        if (o[num] > len(nums)//2):
            return num

# alternate soln 1
# dictKey = Counter(nums)
# maxKey = max(dictKey, key = dictKey.get)
# return maxKey

# alternate soln 2
# nums = sorted(nums)
# o = 0
# for _ in range(len(set(nums))):
#     if(nums.count(nums[o]) > len(nums)//2):
#         return nums[o]
#     else:
#         o += nums.count(nums[o])


nums = [1, 1, 2, 3, 4]
print(majorityElement(nums))
