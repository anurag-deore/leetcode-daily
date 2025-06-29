'''
Problem Name: 2099. Find Subsequence of Length K With the Largest Sum 
Attempted : # 28-06-2025
'''

def maxSubsequence(nums: list[int], k: int) -> list[int]:
    if(len(nums) <= k): return nums
    numsCopy = []
    for i in range(len(nums)):
        numsCopy.append([i,nums[i]])
    numsCopy = sorted(numsCopy, key=lambda x: x[1])[-k:]
    numsCopy = sorted(numsCopy, key=lambda x: x[0])
    result = []
    for n in numsCopy:
        result.append(nums[n[0]])
    return result

print(maxSubsequence([3,3,4,3],2))
print(maxSubsequence([63,-74,61,-17,-55,-59,-10,2,-60,-65],9))