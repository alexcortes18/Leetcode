from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        transversal_order = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            # Pop the node from the stack and add its value to the result
            root = stack.pop()
            transversal_order.append(root.val)

            # Move to the right subtree
            root = root.right

        return transversal_order

if __name__ == "__main__":
    # Create the binary tree [1, null, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    result = solution.inorderTraversal(root)
    print(result)  # Output: [1, 3, 2]
