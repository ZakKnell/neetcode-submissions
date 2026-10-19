# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swapNode(self, parent: Optional[TreeNode]):
        if not parent:
            return 0

        temp = parent.left
        parent.left = parent.right
        parent.right = temp

        if parent.left:
            self.swapNode(parent.left)
        if parent.right:
            self.swapNode(parent.right)
            

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.swapNode(root)
        return root
            