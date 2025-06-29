# https://leetcode.com/problems/add-binary/

def addBinary(a, b):
    result = []
    carry = 0
    n, m = len(a) - 1, len(b) - 1
    while n >= 0 or m >= 0 or carry:
        total = carry
        if(n >= 0):
            total += (int(a[n]))
            n -= 1
        if(m >= 0):
            total += (int(b[m]))
            m -= 1
        result.append(str(total % 2))
        carry = total // 2
    return ''.join(reversed(result))


a = "11"
b = "1"
print(addBinary(a, b))
