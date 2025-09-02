# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      dummy_node = ListNode(-1)
      dummy_node.next = head

      current_node, previous_node = head, dummy_node

      while current_node:
        while current_node.next and current_node.val == current_node.next.val:
          current_node = current_node.next
        
        if previous_node.next == current_node:
          previous_node = previous_node.next
          current_node = current_node.next
        else:
          previous_node.next = current_node.next
          current_node = previous_node.next
      
      return dummy_node.next
