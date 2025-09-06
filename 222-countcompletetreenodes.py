'''
Problem name : 222 countcompletetreenodes
attempted : # 06-07-2025
'''

Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree_depth(self, node: TreeNode) -> int:
        depth = 0
        while node.left:
            node = node.left
            depth += 1
        return depth
    
    def node_exists(self, index: int, depth: int, node: TreeNode) -> bool:
        low, high = 0, 2**depth - 1
        for _ in range(depth):
            mid = low + (high - low) // 2
            if index <= mid:
                node = node.left
                high = mid
            else:
                node = node.right
                low = mid + 1
        return node is not None
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        depth = self.tree_depth(root)
        if depth == 0:
            return 1
            
        low, high = 1, 2**depth - 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.node_exists(mid, depth, root):
                low = mid + 1
            else:
                high = mid - 1
            
        return (2**depth - 1) + low
