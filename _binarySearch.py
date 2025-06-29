def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while (left != right):
        mid = (left+right)//2
        if(arr[mid] == target):
            return mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


arr = [23, 46, 69, 92, 115, 138, 161, 184]
target = 46
res = binarySearch(arr, target)
if res == -1:
    print("Element not found")
else:
    print("Element found at location", res)
