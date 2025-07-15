'''
Problem Name: 2873. Maximum Value of an Ordered Triplet I
Attempted : # 15-07-2025
'''

def maximumTripletValue(nums: list[int]) -> int:
    maxval = 0
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                val = (nums[i] - nums[j]) * nums[k]
                maxval = max(val,maxval)
    return maxval

print(maximumTripletValue([12,6,1,2,7]))