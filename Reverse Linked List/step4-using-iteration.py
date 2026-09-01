# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        new_head_node, current_node = None, head

        while current_node:
            rest_node_head = current_node.next
            current_node.next = new_head_node
            new_head_node = current_node
            current_node = rest_node_head
        return new_head_node
        
