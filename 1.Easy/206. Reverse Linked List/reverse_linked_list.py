from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original_list = []
        while head:
            original_list.append(head)
            head = head.next
        reversed_list = original_list[::-1]
        dummy = ListNode()
        current = dummy
        for node in reversed_list:
            current.next = node
            current = current.next
        current.next = None
        return dummy.next