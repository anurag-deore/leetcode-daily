# https://leetcode.com/problems/first-bad-version/
'''
somewhat similar to binary search
'''

def isBadVersion(version):
    return True

def firstbadversion(n):
    left = 1
    right = n
    while (left < right):
        mid = (left+right)//2
        if(not isBadVersion(mid)):
            left =  mid + 1
        else:
            right = mid
    return left