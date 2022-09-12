from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
    def commented(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if we have no root, base case return None
        if not root:
            return None
        # invert the right and left side
        right = self.commented(root.right)
        left = self.commented(root.left)
        # right = left, left = right
        root.left = right
        root.right = left
        return root