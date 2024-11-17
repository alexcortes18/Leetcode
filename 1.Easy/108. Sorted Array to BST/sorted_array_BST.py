from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values to match desired output format
    while result and result[-1] is None:
        result.pop()
    
    return result

# MOST important function, the one that is tested in Leetcode:
# ------------------------------------------------------------------------------------------------
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
# ------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Example test cases
    solution = Solution()

# Test case 1: Sorted array [1, 2, 3, 4, 5]
    nums1 = [1, 2, 3, 4, 5]
    bst1 = solution.sortedArrayToBST(nums1)
    print("In-order traversal of BST for [1, 2, 3, 4, 5]:", level_order_traversal(bst1))

    # Test case 2: Sorted array [-10, -3, 0, 5, 9]
    nums2 = [-10, -3, 0, 5, 9]
    bst2 = solution.sortedArrayToBST(nums2)
    print("In-order traversal of BST for [-10, -3, 0, 5, 9]:", level_order_traversal(bst2))