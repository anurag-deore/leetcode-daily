# https://leetcode.com/problems/contains-duplicate/
'''
When the int class is passed as the default_factory argument, then a defaultdict is created with default value as zero.

d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
for i in L:     -> Iterate through the list for keeping the count
    d[i] += 1   -> The default value is 0 so there is no need to enter the key first
print(d)        -> defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})
'''
from collections import defaultdict

def containsDuplicate(nums):
    m = defaultdict(int)
    for i in nums:
        if m[i] == 1:
            return True
        m[i] = 1
    return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums))
