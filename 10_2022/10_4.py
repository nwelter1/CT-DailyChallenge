from typing import Optional
# O(n) Time Where n == nodes in tree, O(h) Space where h == avg height of the tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkPath(root, targetSum)
    
    def checkPath(self, root, targetSum, currSum = 0):
        if not root:
            return False
        currSum += root.val
        if not root.left and not root.right:
            if currSum == targetSum:
                return True
            return False
        return self.checkPath(root.left, targetSum, currSum) or self.checkPath(root.right, targetSum, currSum)
            

class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if targetSum == 0 and not root.left and not root.right:
            return True
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


test_1 = TreeNode(5)
test_1.left = TreeNode(4)
test_1.right = TreeNode(8)
test_1.left.left = TreeNode(11)
test_1.left.left.left = TreeNode(7)
test_1.left.left.right = TreeNode(2)
test_1.right.left = TreeNode(13)
test_1.right.right = TreeNode(4)
test_1.right.right.right = TreeNode(1)

test_2 = TreeNode(1)
test_2.left = TreeNode(2)
test_2.right = TreeNode(3)

test_3 = None

s = Solution()
print(s.hasPathSum(test_1, 22), s.hasPathSum(test_2, 5), s.hasPathSum(test_3, 0))
s2 = Solution2()
print(s2.hasPathSum(test_1, 22), s2.hasPathSum(test_2, 5), s2.hasPathSum(test_3, 0))

