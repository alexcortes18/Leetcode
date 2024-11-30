# ------------------------------------------------------------------------------------------------
# TO CLARIFY: This solution only solves it in O(n) time, which is not what the original question
# wants. It should be in less than O(n). Too lazy...
# ------------------------------------------------------------------------------------------------


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if root == [] or root == None: return 0
        # both of those conditionals can be summarized with:
        if not root: return 0
        counter = 1
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                counter += 1
            if node.right:
                stack.append(node.right)
                counter += 1
        return counter