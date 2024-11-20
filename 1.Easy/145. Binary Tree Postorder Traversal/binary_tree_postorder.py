from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        visited = []
        stack = [root]

        if not root:
            return []

        while stack:
            node = stack[-1]

            if node.right and node.right not in visited:
                stack.append(node.right)
            if node.left and node.left not in visited:
                stack.append(node.left)
            
            if (not node.left and not node.right) or \
            ((not node.left or  node.left in visited) and (not node.right or  node.right in visited)):
                visited.append(node)
                answer.append(stack.pop().val)
        return answer

            
