from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # pos = -1
        # stack = []
        # while head:
        #     if head not in stack:
        #         stack.append(head)
        #     else:
        #         pos = stack.index(head)
        #         return True
        #     head = head.next
        # return False

        # ChatGpt help: Floyd's Tortoise and Hare Algorithm
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True
        return False