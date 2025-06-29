# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchRange(nums, target):
    left = 0
    l = [0, 0]
    right = len(nums)-1
    if len(nums) == 1 and target == nums[0]:return [0,0]
    while(left < right):
        if(nums[left] == target and nums[right] == target):
            l[0] = left
            l[1] = right
            return l
        if(nums[left] != target):left+=1
        if(nums[right] != target):right-=1
    if(left == right and nums[left] == target):return [left,right]
    else:return [-1,-1]
        


nums = [1,3,3]
target = 1
print(searchRange(nums, target))
