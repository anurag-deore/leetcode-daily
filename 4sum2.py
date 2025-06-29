# https://leetcode.com/problems/4sum-ii/
'''
'''


def fourSumCount(A, B, C, D):
    o = {}
    ans = 0
    for i in range(0, len(A)):
        for j in range(len(B)):
            if (A[i] + B[j] not in o):
                o[A[i]+B[j]] = 0
            o[A[i]+B[j]] += 1

    for i in range(0, len(C)):
        for j in range(len(D)):
            target = -(C[i] + D[j])
            if (C[i] + D[j] in o):
                ans += o[target]
    return ans


A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(fourSumCount(A, B, C, D))
