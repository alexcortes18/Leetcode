from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None: return True

        left_side = root.left
        right_side = root.right

        if root.left is None or root.right is None: return False
        stack_left = []
        stack_right = []
        while (left_side or stack_left) and (right_side or stack_right):
            while left_side and right_side:
                if left_side.val == right_side.val:
                    stack_left.append(left_side)
                    stack_right.append(right_side)
                    left_side = left_side.left
                    right_side = right_side.right
                else: return False

            if left_side != right_side: return False
            left_side = stack_left.pop()
            right_side = stack_right.pop()

            left_side = left_side.right
            right_side = right_side.left
            
            if left_side is None and right_side: return False
            if right_side is None and left_side: return False

        return True


if __name__ == "__main__":
    # Helper function to build a tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Example test case to debug
    values = [1, 2, 2, 3, 4, 4, 3]  # Symmetric tree
    root = build_tree(values)

    # Testing your implementation
    solution = Solution()
    print("Testing symmetric tree [1, 2, 2, 3, 4, 4, 3]:")
    print("Is symmetric:", solution.isSymmetric(root))

    # Add more test cases
    values = [1, 2, 2, None, 3, None, 3]  # Asymmetric tree
    root = build_tree(values)
    print("\nTesting asymmetric tree [1, 2, 2, None, 3, None, 3]:")
    print("Is symmetric:", solution.isSymmetric(root))
    
    values = [1,2,2,2,None,2]  # Asymmetric tree
    root = build_tree(values)
    print("\nTesting asymmetric tree [1, 2, 2, 2, None, 2]:")
    print("Is symmetric:", solution.isSymmetric(root))
    
    
