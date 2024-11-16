# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----------------------------------------------------------------------------------------------------
# This is the main question problem, the rest is just helpers from ChatGpt to visualize the problem
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while head:
            # Connect the current node and move forward
            current.next = head
            current = current.next

            # Skip all duplicate nodes with the same value
            while head.next and head.val == head.next.val:
                head = head.next

            # Move to the next unique value
            head = head.next

        current.next = None  # Ensure the end of the list is null
        return dummy.next
# ----------------------------------------------------------------------------------------------------


# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Main
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 1, 2, 3, 3],
        [1, 1, 2],
        [1, 2, 2, 3],
        [1, 1, 1],
        [1, 2, 3],
        []
    ]

    solution = Solution()
    for test in test_cases:
        head = create_linked_list(test)
        new_head = solution.deleteDuplicates(head)
        result = linked_list_to_list(new_head)
        print(f"Input: {test} -> Output: {result}")
