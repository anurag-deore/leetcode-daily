'''
Problem Name: 1498. Number of subsequences that satisfy the given sum condition
Attempted : # 29-06-2025
'''

def numSubseq(nums: list[int], target: int) -> int:
  nums.sort()
  res = 0
  mod = (10**9 + 7)

  r = len(nums) - 1
  for i, left in enumerate(nums):
    while (left + nums [r]) > target and i <= r:
      r -= 1
    if i <= r:
      res += (2**(r - i)) % mod
  return res



print(numSubseq([3,5,6,7],9))