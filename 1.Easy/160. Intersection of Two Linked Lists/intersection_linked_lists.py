from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # # Both are one node and equal
        # if headA == headB: return headA

        # # They have different tails so they don't ever connect
        # originalheadA = headA
        # originalheadB = headB
        # headAtail = headA
        # headBtail = headB
        # while headA or headB:
        #     if headA:
        #         # if headA.next:
        #         headAtail = headA
        #         headA = headA.next    
        #     if headB:
        #         # if headB.next:
        #         headBtail = headB
        #         headB = headB.next
        # if headAtail != headBtail: return None


        # headA = originalheadA
        # headB = originalheadB

        # # They might connect at some point
        # headB_starting_node = headB
        # while headA:
        #     while headB:
        #         if headB == headA:
        #             return headA
        #         headB = headB.next
        #     headA = headA.next
        #     headB = headB_starting_node
        # return None

        # CHATGPT ----- much more efficient...

        # Edge case: If either list is empty, there is no intersection
        if not headA or not headB:
            return None

        # Two pointers
        pointerA = headA
        pointerB = headB

        # Traverse both lists; when one pointer reaches the end, switch to the other list
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # Either both pointers meet at the intersection node, or they meet at None
        return pointerA