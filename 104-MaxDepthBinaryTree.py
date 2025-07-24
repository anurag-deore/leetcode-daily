'''
Problem Name: 104. Maximum Depth of Binary Tree
Attempted : # 24-07-2025
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None or root == "null":
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))


s = Solution()
# Helper function to build a binary tree from a list (level order)


def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root


tree1 = build_tree([3, 9, 20, None, None, 15, 7])
tree2 = build_tree([1, None, 2])

print(s.maxDepth(tree1))
print(s.maxDepth(tree2))
