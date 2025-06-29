# https://leetcode.com/problems/container-with-most-water/

def mostwater(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right])*(right-left))
        if(height[left] < height[right]):
            left += 1
        else:
            right -= 1
    return max_area


height = [4, 3, 2, 1, 4]
print(mostwater(height))
