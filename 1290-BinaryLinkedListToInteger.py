'''
Problem Name: 1290. Convert Binary Number in a Linked List to Integer
Attempted : # 14-07-2025
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val = ""
        while True:
            val += str(head.val)
            if head.next == None:
                break
            else:
                head = head.next
        return int(val,2)