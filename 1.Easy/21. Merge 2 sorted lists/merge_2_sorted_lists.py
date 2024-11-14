from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#  Main code for problem from leetcode:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1 #during first iteration current.next is like
                # saying dummy.next. BOTH CHANGE. So we can keep the first element
                # or head of the list with "dummy.next" used in the return.
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        return dummy.next

# EXTRA Code from ChatGPT to run the Solution class:

# Helper function to print linked list
def print_list(node: ListNode):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Helper function to create linked list from a list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Main entry point for testing
if __name__ == "__main__":
    # Example lists to merge
    list1_values = [1, 2, 4]
    list2_values = [1, 3, 4]

    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    print("Merged List:")
    print_list(merged_list)