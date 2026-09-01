# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        new_head = stack.pop()
        tail = new_head

        while stack:
            new_tail = stack.pop()
            tail.next = new_tail
            tail = tail.next
        
        tail.next = None
        return new_head
        
