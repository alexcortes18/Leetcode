from typing import Optional

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

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

if __name__ == "__main__":
    # Helper function to print the tree in-order for testing
    def print_in_order(node):
        if not node:
            return
        print_in_order(node.left)
        print(node.val, end=" ")
        print_in_order(node.right)

    # Test case 1: Simple binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original Tree (in-order):")
    print_in_order(root)

    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("\nInverted Tree (in-order):")
    print_in_order(inverted_root)

    # Test case 2: Single-node tree
    root2 = TreeNode(1)
    print("\n\nOriginal Tree (single node):")
    print_in_order(root2)

    inverted_root2 = solution.invertTree(root2)

    print("\nInverted Tree (single node):")
    print_in_order(inverted_root2)

    # Test case 3: Empty tree
    root3 = None
    print("\n\nOriginal Tree (empty): None")

    inverted_root3 = solution.invertTree(root3)

    print("Inverted Tree (empty):", inverted_root3)
