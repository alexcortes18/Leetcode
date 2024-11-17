from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive implementation:
        # -----------------------------------
        # if root is None:
        #     return 0
        
        # left_node = self.maxDepth(root.left)
        # right_node = self.maxDepth(root.right)
        # return 1+ max(left_node, right_node)

        # queue implementation:
        # -----------------------------------
        queue = [root]
        depth = 0

        if root is None: return 0

        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            depth += 1
        return depth


# Example usage
if __name__ == "__main__":
    # Example 1: Tree: [3, 9, 20, None, None, 15, 7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    # Example 2: Tree: [1, None, 2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    # Create a Solution object
    solution = Solution()

    # Find and print the max depth of each tree
    print("Max depth of tree 1:", solution.maxDepth(root1))  # Output: 3
    print("Max depth of tree 2:", solution.maxDepth(root2))  # Output: 2