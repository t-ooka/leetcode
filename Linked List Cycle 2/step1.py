# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      seen_nodes = set()
      node = head

      while node:
        if node in seen_nodes:
          return node
        seen_nodes.add(node)
        node = node.next
        
      return None
