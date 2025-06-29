# https://leetcode.com/problems/missing-number/
'''
we use gauss formula
for given consecutive numbers:
s = n*(n+1)/2
for the sum of n consecutive elements in a list would be "S"
and if get the sum(nums) with a missing number and subtract both 
we would get the missing number

missing number = expected sum of n numbers - actual sum of given n numbers

'''
def missingNumber(nums):
    n = len(nums)
    return (n*(n+1))//2 - sum(nums)

arr = [9,6,4,2,3,5,7,0,1]
print(missingNumber(arr))