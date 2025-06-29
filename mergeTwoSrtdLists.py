# https://leetcode.com/problems/merge-two-sorted-lists/
'''
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    cur = ListNode(0)
    ans = cur

    while(l1 and l2):
        if(l1.val > l2.val):
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next

    while(l1):
        cur.next = l1
        l1 = l1.next
        cur = cur.next

    while(l2):
        cur.next = l2
        l2 = l2.next
        cur = cur.next

    return ans.next

l1 = [1, 2, 4]
l2 = [1, 3, 4]
print(mergeTwoLists(l1, l2))
