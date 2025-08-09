'''
Problem Name: 228. Summary Ranges
Attempted : # 10-08-2025
'''


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        if not nums:
            return ranges

        start = nums[0]  # Start of current range

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                # End current range
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i-1]}")
                start = nums[i]  # Start new range

        # Handle last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{nums[-1]}")

        return ranges


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
