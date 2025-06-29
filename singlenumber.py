 # https://leetcode.com/problems/single-number/
'''
now 
2c - c = c
2a + 2b + 2c - 2a - 2b - c = c
2(a+b+c) - (2a+2b+c) = c
this gives us:

2(UniqueElements) - (sum of all elements) = element occuring once

'''


def singleNumber(nums):
    l = set(nums)
    return 2*sum(l) - sum(nums)

nums = [4, 2, 1, 2, 1]
print(singleNumber(nums))
