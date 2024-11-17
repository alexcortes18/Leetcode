# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = []
        stack_q = []
        while p or q or stack_p:
            while p and q: 
                if p.val == q.val:
                    stack_p.append(p)
                    stack_q.append(q)
                    p = p.left
                    q = q.left
                else: 
                    return False
            
            if (p is None) != (q is None): 
                return False

            p = stack_p.pop()
            q = stack_q.pop()
            p = p.right
            q = q.right
        return True

if __name__ == "__main__":
    # Example Test Cases

    # Test Case 1: Same tree
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)

    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    solution = Solution()
    print(solution.isSameTree(p1, q1))  # Expected Output: True

    # Test Case 2: Different structure
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    print(solution.isSameTree(p2, q2))  # Expected Output: False

    # Test Case 3: Different values
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)

    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)

    print(solution.isSameTree(p3, q3))  # Expected Output: False
