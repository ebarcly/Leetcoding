# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create two pointers
        slow = head
        fast = head

        # fast pointer is moving twice as fast as slow so we need to check we always have space left to move
        # When fast reaches the end of the list, slow must be in the middle.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow 
