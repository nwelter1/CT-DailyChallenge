from typing import Optional
class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkPath(root, targetSum )
    
    def checkPath(self, root, targetSum, currSum = 0):
        if not root:
            return False
        currSum += root.val
        if not root.left and not root.right:
            if currSum == targetSum:
                return True
            return False
        
        return self.checkPath(root.left, targetSum, currSum) or self.checkPath(root.right, targetSum, currSum)


# Creating test TreeNode 1
test_1 = TreeNode(5)
test_1.left = TreeNode(4)
test_1.right = TreeNode(8)
test_1.left.left = TreeNode(11)
test_1.left.left.left = TreeNode(7)
test_1.left.left.right = TreeNode(2)
test_1.right.left = TreeNode(13)
test_1.right.right = TreeNode(4)
test_1.right.right.right = TreeNode(1)

# Creating test TreeNode 2
test_2 = TreeNode(1)
test_2.left = TreeNode(2)
test_2.right = TreeNode(3)

# creating test 3
test_3 = None

# Calling Tests
s = Solution()

print(s.hasPathSum(test_1, 22),
s.hasPathSum(test_2, 5),
s.hasPathSum(test_3, 0))


