from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while head:
            # print(head.val)
            if head.val != val:
                current.next = head
                current = current.next
            
            head = head.next
        current.next = None
        return dummy.next
    
# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list (for easy visualization)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example to test your `removeElements` function
values = [1, 2, 6, 3, 4, 5, 6]  # Input list
val_to_remove = 6  # Value to remove

# Create the linked list
head = create_linked_list(values)

# Create a solution object and call the method
solution = Solution()
updated_head = solution.removeElements(head, val_to_remove)

# Convert the updated linked list back to a Python list to check the result
result = linked_list_to_list(updated_head)
print("Resulting Linked List:", result)
