# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      slow_node, fast_node = head, head

      while fast_node and fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next

        if slow_node == fast_node:
          fast_node = head

          while fast_node != slow_node:
            fast_node = fast_node.next
            slow_node = slow_node.next
          
          return fast_node
      
      return None
       
